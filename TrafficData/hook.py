import time
import frida
import zlib 

device = frida.get_usb_device() 

# 直接启动对应的 APP
# pid = device.spawn("com.snail.android.lucky")
# device.resume(pid) 
# 使用 frida-ps -Uia 获取 APP 的 PID

pid = 16673 
print(pid) 

# time.sleep(1) 
session = device.attach(pid)
with open("hook.js") as f:    
    script = session.create_script(f.read()) 
    
def show_data(headers, payload):    
    try:        
        _headers = headers.decode('utf-8')        
        headers = _headers    
    except:        
        pass     
    try:        
        _payload = payload.decode('utf-8')        
        payload = _payload    
    except:        
        pass     
    
    print(headers, '\n\n', payload) 
    
# “请求-响应”对，使用 SSL 句柄作为 KEY

pairs = dict()
def on_message(message, payload):    
    # print(message, payload)    
    if message['type'] != 'send':        
        return     
    ssl = message['payload']['ssl']    
    if message['payload']['code'] == 100: # SSL_write        
        pairs[ssl] = dict()        
        pairs[ssl]['w'] = payload    
    elif message['payload']['code'] == 200: # SSL_read        
        # print(ssl)        
        if ssl not in pairs:            
            return         
        # 响应分段合并        
        if payload.find(b'HTTP') == 0: # 首段            
            pairs[ssl]['r'] = bytearray(payload)        
        else: # 后面的分段            
            if 'r' not in pairs[ssl]:                
                del pairs[ssl]                
                return             
            pairs[ssl]['r'].extend(payload)         

#########################################################################################################################################################         

        r_headers = bytes()        
        r_payload = bytes()       
        _parts = pairs[ssl]['r'].split(b'\r\n\r\n', 1)        
        if len(_parts) != 2:            
            del pairs[ssl]            
            print('read parts length err =', len(_parts))            
            return         
        
        # 尝试解压已接收到的响应数据        
        if _parts[0].find(b'Content-Encoding: gzip') >= 0:            
            _data = bytearray()            
            _gzip = _parts[1].split(b'\r\n')            
            for i in range(1, len(_gzip), 2): # 跳过长度                
                _data.extend(_gzip[i])             
            try:                
                _data = zlib.decompress(_data, 16 + zlib.MAX_WBITS)            
            except: # 可能是响应还未接收完                
                return             
            
            r_headers = _parts[0]            
            r_payload = _data        
        else: # 无需解压            
            r_headers = _parts[0]            
            r_payload = _parts[1]        

#########################################################################################################################################################         
        w_headers = bytes()        
        w_payload = bytes()        
        _parts = pairs[ssl]['w'].split(b'\r\n\r\n', 1)        
        if len(_parts) != 2:            
            del pairs[ssl]            
            print('write parts length err =', len(_parts))            
            return         
        
        # 尝试解压已接收到的请求数据        
        if _parts[0].find(b'Content-Encoding: gzip') >= 0:            
            _data = bytearray()            
            try:                
                _data = zlib.decompress(_parts[1], 16 + zlib.MAX_WBITS)            
            except:                
                del pairs[ssl]                
                print('write payload decompress err =', _parts[1])                
                return             
            w_headers = _parts[0]            
            w_payload = _data        
        else: # 无需解压            
            w_headers = _parts[0]            
            w_payload = _parts[1]         
            print('*' * 120)        
            show_data(w_headers, w_payload)        
            print('\n')        
            show_data(r_headers, r_payload)        
            print('*' * 120)        
            del pairs[ssl] 
            
script.on("message", on_message)
script.load()
input() #等待输入 
session.detach()    
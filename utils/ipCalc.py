import ipcalc

def getIP(ip):
    try: 
        calc = ipcalc.Network(ip);

        data = f'''ip : {ip}
netmask : {calc.netmask()}
network : {calc.network()}
broadcast : {calc.broadcast()}
range : {calc.host_first()} - {calc.host_last()}'''
        return data;
        
    except:
        return f'({ip}) format IP salah Blok.....!';
    

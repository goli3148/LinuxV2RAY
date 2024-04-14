from path import paths

import json

def editConfigFile(protocol='vless', address='fr.v2landsshop.top',
                   port=36887, uid='95975b55-40e9-4338-90ba-7c244e63bd7d',
                   host='speedtest.net', headerType='http', networkType='tcp'):
    
    config_path = paths()['config']
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    config['outbounds'][0]['protocol'] = protocol
    config['outbounds'][0]['settings']['vnext'][0]['address'] = address
    config['outbounds'][0]['settings']['vnext'][0]['port'] = port
    config['outbounds'][0]['settings']['vnext'][0]['users'][0]['id'] = uid
    config['outbounds'][0]['streamSettings']['tcpSettings']['header']['request']['headers']['Host'] = [host]
    config['outbounds'][0]['streamSettings']['tcpSettings']['header']['type'] = headerType
    config['outbounds'][0]['streamSettings']['network'] = networkType

    with open(config_path, 'w') as file:
        json.dump(config, file, indent=2)

def ExportConfigFile():
    config_path = paths()['config']
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    return {
        "protocol": config['outbounds'][0]['protocol'],
        "address": config['outbounds'][0]['settings']['vnext'][0]['address'],
        "port": config['outbounds'][0]['settings']['vnext'][0]['port'],
        "uid": config['outbounds'][0]['settings']['vnext'][0]['users'][0]['id'],
        "host": config['outbounds'][0]['streamSettings']['tcpSettings']['header']['request']['headers']['Host'],
        "header_type": config['outbounds'][0]['streamSettings']['tcpSettings']['header']['type'],
        "network_type": config['outbounds'][0]['streamSettings']['network']
    }


import json

def parse_interface_data(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    print("Interface Status")
    print("=" * 80)
    dn_char_length = 50
    descr_char_length = 20
    speed_char_length = 8
    mtu_char_length = 6
    print(f"{'DN':<{dn_char_length}} {'Description':<{descr_char_length}} {'Speed':<{speed_char_length}} {'MTU':<{mtu_char_length}}")
    print(f"{'-' * dn_char_length} {'-' * descr_char_length} {'-' * speed_char_length} {'-' * mtu_char_length}")
    
    for item in data.get('imdata', []):
        if 'l1PhysIf' in item:
            attributes = item['l1PhysIf']['attributes']
            
            dn = attributes.get('dn', '')
            descr = attributes.get('descr', '')
            speed = attributes.get('speed', '')
            mtu = attributes.get('mtu', '')
            
            print(f"{dn:<{dn_char_length}} {descr:<{descr_char_length}} {speed:<{speed_char_length}} {mtu:<{mtu_char_length}}")

json_file_path = "sample_data.json"
parse_interface_data(json_file_path)
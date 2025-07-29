import requests
from ipwhois import IPWhois

def get_whois_info(ip):
    obj = IPWhois(ip)
    data = obj.lookup_rdap()
    return {
        "ASN": data.get("asn"),
        "Organization": data["network"].get("name"),
        "CIDR": data["network"].get("cidr"),
        "Country": data["network"].get("country"),
        "ASN Description": data.get("asn_description"),
    }

def get_geolocation(ip):
    res = requests.get(f"http://ip-api.com/json/{ip}")
    if res.status_code == 200:
        data = res.json()
        return {
            "City": data.get("city"),
            "Region": data.get("regionName"),
            "Country": data.get("country"),
            "ISP": data.get("isp"),
            "Latitude": data.get("lat"),
            "Longitude": data.get("lon")
        }
    return {}

def save_to_txt(ip, whois_data, geo_data):
    filename = f"{ip.replace('.', '_')}_info.txt"
    with open(filename, "w") as f:
        f.write(f"IP Address: {ip}\n")
        f.write("\n[WHOIS Information]\n")
        for key, value in whois_data.items():
            f.write(f"{key}: {value}\n")
        f.write("\n[Geolocation Information]\n")
        for key, value in geo_data.items():
            f.write(f"{key}: {value}\n")
    print(f"[+] IP details saved to {filename}")

def main():
    ip = input("[+] Enter the target IP: ")
    print(f"[+] Gathering data for {ip}...")

    whois_data = get_whois_info(ip)
    geo_data = get_geolocation(ip)
    save_to_txt(ip, whois_data, geo_data)

if __name__ == "__main__":
    main()

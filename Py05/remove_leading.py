def remove_leading(ip):
    return ".".join(map(lambda x: str(int(x)), ip.split('.')))
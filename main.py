import os, re, gzip, base64


dat_path  = os.path.join(os.getenv('LocalAppData'), 'GeometryDash', 'CCGameManager.dat')
xml_path  = "CCGameManager.txt"
mana_orbs = "0"
diamonds  = "0"
demon_kys = "0"


def decrypt():
    data              = open(dat_path, "rb").read(((os.path.getsize(dat_path) // 4) * 4))

    xor_data          = bytes(b ^ 0x0B for b in data)
    decoded_data      = base64.urlsafe_b64decode(xor_data)
    decompressed_data = gzip.decompress(decoded_data)

    with open(xml_path, "w", encoding="utf-8") as f:
        f.write(decompressed_data.decode())


def mod():
    data          = open(xml_path, "r", encoding="utf-8").read()

    modified_data = re.sub(r'GS_11(.*?)</i></d></d></d></d><k>', f"GS_11</k><d><k>2_3</k><d><k>kCEK</k><i>8</i><k>1</k><i>3</i><k>2</k><i>2</i><k>3</k><d><k>_isArr</k><t /><k>k_0</k><d><k>kCEK</k><i>9</i><k>1</k><i>7</i><k>3</k><i>{mana_orbs}</i></d><k>k_1</k><d><k>kCEK</k><i>9</i><k>1</k><i>8</i><k>3</k><i>{diamonds}</i></d><k>k_2</k><d><k>kCEK</k><i>9</i><k>1</k><i>1</i><k>3</k><i>1</i><k>4</k><i>540</i></d><k>k_3</k><d><k>kCEK</k><i>9</i><k>1</k><i>3</i><k>3</k><i>1</i><k>4</k><i>7171939</i></d></d></d><k>1_3</k><d><k>kCEK</k><i>8</i><k>1</k><i>3</i><k>2</k><i>1</i><k>3</k><d><k>_isArr</k><t /><k>k_0</k><d><k>kCEK</k><i>9</i><k>1</k><i>6</i><k>3</k><i>{demon_kys}</i><k>4</k><i>540</i></d><k>k_1</k><d><k>kCEK</k><i>9</i><k>1</k><i>8</i><k>3</k><i>0</i></d></d></d></d><k>", data, flags=re.DOTALL)

    with open(xml_path, "w", encoding="utf-8") as f:
        f.write(modified_data)


def encrypt():
    data            = open(xml_path, "r", encoding="utf-8").read()

    compressed_data = gzip.compress(data.encode())
    encoded_data    = base64.urlsafe_b64encode(compressed_data)
    xor_data        = bytes(b ^ 0x0B for b in encoded_data)

    with open(dat_path, "wb") as f:
        f.write(xor_data)


def main():
    decrypt()
    mod()
    encrypt()
    print("Decrypted, Replaced, Encrypted")
    os.remove(xml_path)


if __name__ == "__main__":
    main()
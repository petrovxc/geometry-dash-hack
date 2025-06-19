# Geometry Dash Custom Currencies

My School Project for my finals exam for [Geometry Dash](https://store.steampowered.com/app/322170/Geometry_Dash/). As used in the presentation.

![alt text](https://raw.githubusercontent.com/petrovxc/geometry-dash-hack/refs/heads/main/screen.png)

Uploaded and working (19/06/25)

#### How this works
Coded in python, I reversed the Geometry Dash Save File, where all data is stored and changed the content of the first two chests opened on the account. This allows anyone to customize the ammount of ingame resources and enjoy the game to it's full potential.

#

If you have any questions on the Geometry Dash Save File check out [this link](https://wyliemaster.github.io/gddocs/#/resources/client/gamesave)!

## Customize Section:

In lines 6-9 in main.py change the zeros to any custom currency:

```py
mana_orbs = "0"
diamonds  = "0"
demon_kys = "0"
```

It uses XOR to decrypt the file, then base64-decodes and decompresses it with GZIP to get readable data. After modifying the values, it compresses, encodes, and re-encrypts the data to restore the original format.

Here it customizes the chest's contents, you can change this to other ingame currencies aswell.
```
def mod():
    data          = open(xml_path, "r", encoding="utf-8").read()

    modified_data = re.sub(r'GS_11(.*?)</i></d></d></d></d><k>', f"GS_11</k><d><k>2_3</k><d><k>kCEK</k><i>8</i><k>1</k><i>3</i><k>2</k><i>2</i><k>3</k><d><k>_isArr</k><t /><k>k_0</k><d><k>kCEK</k><i>9</i><k>1</k><i>7</i><k>3</k><i>{mana_orbs}</i></d><k>k_1</k><d><k>kCEK</k><i>9</i><k>1</k><i>8</i><k>3</k><i>{diamonds}</i></d><k>k_2</k><d><k>kCEK</k><i>9</i><k>1</k><i>1</i><k>3</k><i>1</i><k>4</k><i>540</i></d><k>k_3</k><d><k>kCEK</k><i>9</i><k>1</k><i>3</i><k>3</k><i>1</i><k>4</k><i>7171939</i></d></d></d><k>1_3</k><d><k>kCEK</k><i>8</i><k>1</k><i>3</i><k>2</k><i>1</i><k>3</k><d><k>_isArr</k><t /><k>k_0</k><d><k>kCEK</k><i>9</i><k>1</k><i>6</i><k>3</k><i>{demon_kys}</i><k>4</k><i>540</i></d><k>k_1</k><d><k>kCEK</k><i>9</i><k>1</k><i>8</i><k>3</k><i>0</i></d></d></d></d><k>", data, flags=re.DOTALL)

    with open(xml_path, "w", encoding="utf-8") as f:
        f.write(modified_data)
```

#### Set Up

Python and Geometry Dash, no other dependencies.

If you have further questions open an issue and I'll gladly help :)
#

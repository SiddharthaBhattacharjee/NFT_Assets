import json
base_url = 'https://raw.githubusercontent.com/warengonzaga/nft-dummy-assets/refs/heads/main/src/collections/emoji-nft/images/'

for i in range(1000):
    with open(f'./{i}.json','w') as f:
        dict_data = {
            "name": f"My NFT #{i}",
            "description": f"This is NFT {i} of Collection MyNFT.",
            "image": f"{base_url}{i}.png"
        }
        data = json.dumps(dict_data, indent=4)
        f.write(data)
# pc端钉钉申请的token
dingding_token = "https://oapi.dingtalk.com/robot/send?access_token=168a05904c78d41de1ac1ddd3bb2cebc2bfad3af086ad97577193f100ba1db7e"           # 必填
# ---- 区块浏览器申请的apikey ----
apikey_FTM = "9SMXP3JRUCGF7JK9QC4SAZJINRXVFBSA8G"               #必填
apikey_MATIC = "GCYUJ7BHID5P3PGWKZ5TPKEQS32HBNWZNI"             #必填
apikey_BSC = "MBV47NE6F8SMKHS5W1GKB8P3TFV3KB4ISF"               #必填
apikey_ETH = "P7W5IXUCHRZHIHF6CUTCY2XTC54K61ZH6I"               #必填
apikey_AVAX = "DTZR4D7R1UZZHJUCGPDBSJ82G6T8SGT6TA"              #必填

# 填写需要监控的地址
oxdata = {
    "0x5028d77b91a3754fb38b2fbb726af02d1fe44db6": "0xb1早期defi大神",
    "0xb1adceddb2941033a090dd166a462fe1c2029484": "0xb1早期defi大神",
    "0x85560dbef2533eec139b3e206b119fd700f90262": "冯波",
    "0x5338035c008ea8c4b850052bc8dad6a33dc2206c": "NFT高级玩家@推特MEV Collecto",
    "0xd2db6c5e613c0e1ce63c7a15045e8d163a3fc576": "王峰火星财经、NFT交易平台Element创始人",
    "0xd387a6e4e84a6c86bd90c158c6028a58cc8ac459": "白手起家NFT高级玩家Pranksy",
    "0xc79b1cb9e38af3a2dee4b46f84f87ae5c36c679c": "白手起家NFT高级玩家Pranksy",
    "0x220866b1a2219f40e72f5c628b65d54268ca3a9d": "V神",
    "0xab5801a7d398351b8be11c439e05c5b3259aec9b": "V神",
    "0x1db3439a222c519ab44bb1144fc28167b4fa6ee6": "V神",
    "0x84d34f4f83a87596cd3fb6887cff8f17bf5a7b83": "SBF",
    "0xc5ed2333f8a2C351fCA35E5EBAdb2A82F5d254C3": "SBF",
    "0xb718727e7c8a4646d41d8b0be5e8e2c028b9efaa": "庄重",
    "0x577ebc5de943e35cdf9ecb5bbe1f7d7cb6c7c647": "Cryptopunk大收藏家",
    "0x42f9134e9d3bf7eee1f8a5ac2a4328b059e7468c": "Synthetix创始人Kain",
    "0x7ee09c11d6dc9684d6d5a4c6d333e5b9e336bb6c": "LDO巨鲸1",
    "0x8b1674a617f103897fb82ec6b8eb749ba0b9765b": "LDO鲸鱼2",
    "0x11099ac9cc097d0c9759635b8e16c6a91ecc43da": "LDO鲸鱼3",
    "0x32254b28f793cc18b3575c86c61fe3d7421cbbef": "LDO鲸鱼4",
    "0xfd22004806a6846ea67ad883356be810f0428793": "NFT收藏家",
    "0xe6754b5ee999c875ff4b8299cf7ddb3532e6f2ef": "企鹅NFT鲸鱼",
    "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae": "以太坊基金会",
    "0x39cc9c86e67baf2129b80fe3414c397492ea8026": "NFT收藏家",
    "0x6cf9aa65ebad7028536e353393630e2340ca6049": "匿名鲸鱼",
    "0x577eBC5De943e35cdf9ECb5BbE1f7D7CB6c7C647": "NFT cryptopunk loot早期玩家",
    "0x3ddfa8ec3052539b6c9549f12cea2c295cff5296": "justin sun",
    "0x4c8cfe078a5b989cea4b330197246ced82764c63": "Alameda",
    "0x8e04af7f7c76daa9ab429b1340e0327b5b835748": "三箭资本",
    "0x085af684acdb1220d111fee971b733c5e5ae6ccd": "三箭资本",
    "0x4862733b5fddfd35f35ea8ccf08f5045e57388b3": "三箭资本",
    "0x05e793ce0c6027323ac150f6d45c2344d28b6019": "a16z",
    "0xe05a884d4653289916d54ce6ae0967707c519879": "Arca",
    "0xafa64cca337efee0ad827f6c2684e69275226e90": "CMS",
    "0xc8d328b21f476a4b6e0681f6e4e41693a220347d": "Multicoin Capital",
    "0x5028d77b91a3754fb38b2fbb726af02d1fe44db6": "ParaFi",
    "0x4655b7ad0b5f5bacb9cf960bbffceb3f0e51f363": "ParaFi",
    "0xd9b012a168fb6c1b71c24db8cee1a256b3caa2a2": "ParaFi",
    "0xca436e14855323927d6e6264470ded36455fc8bd": "神鱼",
    "0x6e9fe041e0ba8c2af35215d900d188d53d7a9b41": "神鱼nft收藏号"

}
#接收方的智能合约地址，方便查阅
contract_list = {
    "0x10ed43c718714eb63d5aa57b78b54704e256024e":"pancake routerV2",
    "0x95c78222b3d6e262426483d42cfa53685a67ab9d":"Venus: vBUSD Token",
    "0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31":"Metamask: Swap Router",
    "0xe9e7cea3dedca5984780bafc599bd69add087d56":"Binance: BUSD Stablecoin",
    "0x8f8dd7db1bda5ed3da8c9daf3bfa471c12d58486":"Dodoex: V2 Proxy",
    "0x7be8076f4ea4a4ad08075c2508e481d6c946d12b":"Opensea"
}
# 当前transfer的方式
method_data = {
    "0x095ea7b3":"Approve",
    "0x7ff36ab5":"Swap Exact ETH For Tokens",
    "0x18cbafe5":"Swap Exact Token For ETH",
    "0x":"Transfer",
    "0xf305d719":"Add Liquiity ETH",
    "0xfb3bdb41":"Swap ETH For Exact Tokens",
    "0xa22cb465":"setApprovalForAll",
    "0xab834bab":"atomicMatch_(buy_nft)"
}





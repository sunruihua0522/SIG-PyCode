
if __name__ == '__main__':
    from WechatAccount import WechatAccount
    weChatAccount = WechatAccount('联想微信公众号')

    from WechatClientA import WeChatClientA
    user1 = WeChatClientA('用户1')
    user2 = WeChatClientA('用户2')
    user3 = WeChatClientA('用户3')
    user4 = WeChatClientA('用户4')

    weChatAccount.AddClient(user1)
    weChatAccount.AddClient(user2)
    weChatAccount.AddClient(user3)
    weChatAccount.AddClient(user4)

    weChatAccount.Publish('钢铁是怎样练成的')

    print('---------------------------\r\n\r\n')
    weChatAccount.RemoveClient(user2)
    weChatAccount.RemoveClient(user3)
    weChatAccount.Publish('钢铁是怎样练成的第二部')

    pass
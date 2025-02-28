"""
channel factory
"""
from common import const

def create_channel(channel_type):
    """
    create a channel instance
    :param channel_type: channel type code
    :return: channel instance
    """
    if channel_type== const.TERMINAL:
        from channel.terminal.terminal_channel import TerminalChannel
        return TerminalChannel()

    if channel_type == const.WECHAT:
        from channel.wechat.wechat_channel import WechatChannel
        return WechatChannel()

    elif channel_type == const.WECHAT_MP:
        from channel.wechat.wechat_mp_channel import WechatSubsribeAccount
        return WechatSubsribeAccount()

    elif channel_type == const.WECHAT_MP_SERVICE:
        from channel.wechat.wechat_mp_service_channel import WechatServiceAccount
        return WechatServiceAccount()

    elif channel_type == const.GMAIL:
        from channel.gmail.gmail_channel import GmailChannel
        return GmailChannel()

    else:
        raise RuntimeError

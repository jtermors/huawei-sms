from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection
from huawei_lte_api.enums.sms import BoxTypeEnum
from huawei_lte_api.enums.sms import TextModeEnum

connection = AuthorizedConnection('http://admin:password@192.168.8.1/')
client = Client(connection)

#Read SMS
#sms = client.sms.get_sms_list(1, BoxTypeEnum.LOCAL_INBOX, 1, 0, 0, 1)
#print(sms)

print(client.sms.config())
print(client.sms.send_sms([1144], "SALDO"))

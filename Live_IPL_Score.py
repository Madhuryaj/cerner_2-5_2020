import sports #cerner_2^5_2020
from pynotifier import Notification

Match_Infomation=sports.get_sport("CRICKET")
Notification(title="IPL Live Score Updates",description=str(Match_Infomation),duration=10).send() #cerner_2^5_2020

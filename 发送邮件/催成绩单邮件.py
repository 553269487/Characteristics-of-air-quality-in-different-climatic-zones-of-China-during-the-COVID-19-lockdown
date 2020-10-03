import yagmail,time
yagmail.register('553269487@qq.com', 'oshdhxkhqvxtbeie')
yag = yagmail.SMTP('553269487@qq.com', host='smtp.qq.com', port='465')
word="<p>Dear Officer,    </p><p>Hope this email finds you well. you can cc to qihang.dai@student.manchester.    This is Qihang Dai, ID 10578812. I am ready to apply for US graduate school this Fall, which requests Official transcript together with scoring criteria from the University of Manchester. Please kindly provide me with the aforementioned materials at your earliest convenience. Thank you so much! I understand the large amout of email coming in and How busy you are. But I have been keep sending for a week.</p><p>Best,  QIHANG</p>"

localtime = time.asctime( time.localtime(time.time()))

def loopd():
    n=0
    while True:
        # yag.send('ssc@manchester.ac.uk', '10578812 Transcript Urgent',word)
        yag.send('ssc@manchester.ac.uk', '10578812 Transcript Support!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Urgent',word)
        n=n+1
        print(n, 'mail out',time.asctime( time.localtime(time.time())))
        time.sleep(60*5)


try:
    loopd()
except:
    loopd()
print('endtime=',time.asctime( time.localtime(time.time())))


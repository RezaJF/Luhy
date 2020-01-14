import smtplib
import email
import time
import alarm_setting


class sent_work:
    def __init__(self,user_list,title='[Warning]',message_content=''):
        
        if len(user_list[0]) == 1: #str 
            self.user_list = [user_list]
        else:
            self.user_list = user_list
        self.title = title
        self.message_content = message_content
        self.send()
    
    def send(self):
        sender = "lilab_muta@suda.edu.cn"
        user_list = self.user_list

        for user in user_list:
            msg = email.message_from_string(self.message_content)
            msg["subject"] = self.title
            msg["from"] = sender
            msg["to"] = user
            server = smtplib.SMTP('smtp.suda.edu.cn')
            server.login(sender,alarm_setting.email_server_pwd)
            server.sendmail(sender, user, msg.as_string())
            server.quit()

def send_email(reminder_type):
    user_list = alarm_setting.admin_list
    alarm_type_list = alarm_setting.alarm_type_list
    if reminder_type in alarm_type_list:
        title,message_content = alarm_setting.get_email_content(reminder_type)
        sent_work(user_list,title,message_content)




def test():

    user_list = ['185180124@qq.com','liuyimusictc@163.com']
    test = 'python test'
    message_content = 'hello world'
    sent_work(user_list,test,message_content)

def test_time():
    new_text =[]
    now_s = time.time()
    f = open('/data/webservice/reminder/time_reminder.csv','r')
    ls = f.readlines()[1:]
    for l in ls:
        l = l.strip()
        temp = l.split(',')
        reminder_type = temp[0]
        time_str = temp[1]
        has_done = temp[2]
        if has_done == '0':
            #print(time_str)
            timeArray = time.strptime(time_str, "%Y/%m/%d %H:%M")
            timeStamp = int(time.mktime(timeArray))
            #print(timeArray)
            #print(timeStamp)
            if now_s > timeStamp:
                print(reminder_type)
                print('send ' ,reminder_type)
                send_email(reminder_type)
                has_done = '1'
        new_l = reminder_type + ',' + time_str + ',' + str(has_done) + '\n'
        new_text.append(new_l)
    f.close()
    ff = open('/data/webservice/reminder/time_reminder.csv','w')
    ff.write('alarm_type,time,has_done\n')
    for text in new_text:
    	ff.write(text)
    ff.close()
    


def main():
    #test_email()
    test_time()

if __name__ == '__main__':
    main()
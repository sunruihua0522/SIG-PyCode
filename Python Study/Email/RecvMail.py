import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value

def print_info(msg, indent=0):
    str = ''
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            print_info(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
            str = str + content
        else:
            print('%sAttachment: %s' % ('  ' * indent, content_type))
    return str

email_addr = '715751360@qq.com'
password = 'sxdrgmkcrlhgbffh'
pop3_server = 'pop.qq.com'

server = poplib.POP3_SSL(pop3_server,995)
server.user(email_addr)
server.pass_(password)
server.set_debuglevel(1)

print(server.getwelcome())
print(server.stat())
respons, mails, octets = server.list()

print(mails)
print('未读邮件%d封'%len(mails))

#解析第一封邮件
resp, lines, octets = server.retr(6)
msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)

c = print_info(msg)

file = open(file = '25.html',mode = 'x',encoding = 'utf-8')
file.write(c)
file.close()
server.quit()

exit()
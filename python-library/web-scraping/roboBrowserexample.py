import re
from robobrowser import RoboBrowser

br = RoboBrowser()
br.open('https://robinhood.com/login')
form = br.get_form()
form['username'] = 'lpl060695@gmail.com'
form['password'] = 'Loveling0210'
br.submit_form(form)

src = str(br.parsed())

start = '<div class="css-1qd1r5f">'
end = '</div>'

result = re.search('%s(.*)%s' %  (start,end), src).group(1)

print(result)
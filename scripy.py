from requests import get

print "Enter User Name:",
user = raw_input()

req = get('https://codeforces.com/api/user.rating?handle=' + user)

dat = req.json()

if dat['status'] == 'Failed':
    print 'User Not Found'
else:
    # print dat
    for j in dat['result']:
        print j['contestName'], j['contestId'],  j['rank']

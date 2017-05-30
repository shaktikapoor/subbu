import subaruwlst
from passwd import mkpasswd

domCfg = subaruwlst.domainConfig()

connect(domCfg.adminUser(), domCfg.adminPass(), 't3://%s:%s' % (domCfg.servers[domCfg.adminServer]['listen_address'],domCfg.servers[domCfg.adminServer]['listen_port']))

serverConfig()

sr = cmo.getSecurityConfiguration().getDefaultRealm()
rm = sr.lookupRoleMapper('XACMLRoleMapper')
atnr=sr.lookupAuthenticationProvider('DefaultAuthenticator')

user, passwd = 'rallag', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'vxabarat', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'vxliqrbon', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'bdavis', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'vxfahgdel', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'pkumar', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'snajem', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'vxfirspol', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'asax', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'sswa', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'kth1', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'pvad', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'vveera', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)


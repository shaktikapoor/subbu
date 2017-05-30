import subaruwlst
from passwd import mkpasswd

domCfg = subaruwlst.domainConfig()

connect(domCfg.adminUser(), domCfg.adminPass(), 't3://%s:%s' % (domCfg.servers[domCfg.adminServer]['listen_address'],domCfg.servers[domCfg.adminServer]['listen_port']))

serverConfig()

sr = cmo.getSecurityConfiguration().getDefaultRealm()
rm = sr.lookupRoleMapper('XACMLRoleMapper')
atnr=sr.lookupAuthenticationProvider('DefaultAuthenticator')

userlist = ['jzhu']

for user in userlist:
	passwd = mkpasswd()
	atnr.createUser(user, passwd, user)
	atnr.addMemberToGroup('Middleware-App-Developer',user)
	print "%s	%s" % (user, passwd)


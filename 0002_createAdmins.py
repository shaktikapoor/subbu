import subaruwlst
from passwd import mkpasswd

domCfg = subaruwlst.domainConfig()

connect(domCfg.adminUser(), domCfg.adminPass(), 't3://%s:%s' % (domCfg.servers[domCfg.adminServer]['listen_address'],domCfg.servers[domCfg.adminServer]['listen_port']))

serverConfig()

sr = cmo.getSecurityConfiguration().getDefaultRealm()
rm = sr.lookupRoleMapper('XACMLRoleMapper')
atnr=sr.lookupAuthenticationProvider('DefaultAuthenticator')

user, passwd = 'rmi3', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-Admin',user)
print "%s	%s" % (user, passwd)

user, passwd = 'dmar', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-Admin',user)
print "%s	%s" % (user, passwd)

user, passwd = 'jgib', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-Admin',user)
print "%s	%s" % (user, passwd)


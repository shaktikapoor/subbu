import subaruwlst
from passwd import mkpasswd

domCfg = subaruwlst.domainConfig()

connect(domCfg.adminUser(), domCfg.adminPass(), 't3://%s:%s' % (domCfg.servers[domCfg.adminServer]['listen_address'],domCfg.servers[domCfg.adminServer]['listen_port']))

serverConfig()

sr = cmo.getSecurityConfiguration().getDefaultRealm()
rm = sr.lookupRoleMapper('XACMLRoleMapper')
atnr=sr.lookupAuthenticationProvider('DefaultAuthenticator')

user, passwd = 'appdev_testuser', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Developer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'appdeployer_testuser', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Deployer',user)
print "%s	%s" % (user, passwd)

user, passwd = 'appops_testuser', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-App-Operator',user)
print "%s	%s" % (user, passwd)

user, passwd = 'monitors_testuser', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-Monitor',user)
print "%s	%s" % (user, passwd)

user, passwd = 'ops_testuser', mkpasswd()
atnr.createUser(user, passwd, user)
atnr.addMemberToGroup('Middleware-Operator',user)
print "%s	%s" % (user, passwd)

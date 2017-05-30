import subaruwlst

def appendToRoleExpr(role, appendExpr):
    expr = rm.getRoleExpression(None,role)
    print "Current %s global role expression: %s" % (role, expr)
    if appendExpr in expr:
        print "Looks like new clause is already part of expression--skipping"
    else:
        expr = expr+appendExpr
        rm.setRoleExpression(None,role,expr)
        print "New %s global role expression: %s" % (role, expr)
    print

domCfg = subaruwlst.domainConfig()

connect(domCfg.adminUser(), domCfg.adminPass(), 't3://%s:%s' % (domCfg.servers[domCfg.adminServer]['listen_address'],domCfg.servers[domCfg.adminServer]['listen_port']))

serverConfig()

sr = cmo.getSecurityConfiguration().getDefaultRealm()
rm = sr.lookupRoleMapper('XACMLRoleMapper')
atnr=sr.lookupAuthenticationProvider('DefaultAuthenticator')

## Middleware-Admin

## Middleware-App-Developer
appendToRoleExpr('IntegrationDeployer','|Grp(Middleware#DApp#DDeveloper)')

## Middleware-App-Deployer
appendToRoleExpr('Deployer','|Grp(Middleware#DApp#DDeployer)')
#grantAppRole('Service_Bus_Console','ApplicationOperator','weblogic.security.principal.WLSGroupImpl','Middleware-App-Deployer')

## Middleware-App-Operator
#appendToRoleExpr('Monitor','|Grp(Middleware#DApp#DOperator)')

## Middleware-Monitor
#appendToRoleExpr('Monitor','|Grp(Middleware#DMonitor)')

## Middleware-Operator


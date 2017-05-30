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
atnr.createGroup('Middleware-Admin','Middleware System Administrators')
appendToRoleExpr('Admin','|Grp(Middleware#DAdmin)')
appendToRoleExpr('IntegrationAdmin','|Grp(Middleware#DAdmin)')
grantAppRole('soa-infra','SOAAdmin','weblogic.security.principal.WLSGroupImpl','Middleware-Admin')
#grantAppRole('BamServer','BAMAdministrator','weblogic.security.principal.WLSGroupImpl','Middleware-Admin')
grantAppRole('Service_Bus_Console','MiddlewareAdministrator','weblogic.security.principal.WLSGroupImpl','Middleware-Admin')

## Middleware-App-Developer
atnr.createGroup('Middleware-App-Developer','Middleware Application Developer')
appendToRoleExpr('Deployer','|Grp(Middleware#DApp#DDeveloper)')
appendToRoleExpr('IntegrationDeployer','|Grp(Middleware#DApp#DDeveloper)')
#grantAppRole('BamServer','BAMArchitect','weblogic.security.principal.WLSGroupImpl','Middleware-App-Developer')
#grantAppRole('BamServer','IInsightContentViewer','weblogic.security.principal.WLSGroupImpl','Middleware-App-Developer')
grantAppRole('Service_Bus_Console','Developer','weblogic.security.principal.WLSGroupImpl','Middleware-App-Developer')

## Middleware-App-Deployer
atnr.createGroup('Middleware-App-Deployer','Middleware Application Deployer')
appendToRoleExpr('Deployer','|Grp(Middleware#DApp#DDeployer)')
appendToRoleExpr('IntegrationDeployer','|Grp(Middleware#DApp#DDeployer)')
#grantAppRole('BamServer','BAMArchitect','weblogic.security.principal.WLSGroupImpl','Middleware-App-Deployer')
#grantAppRole('BamServer','IInsightContentViewer','weblogic.security.principal.WLSGroupImpl','Middleware-App-Deployer')
grantAppRole('Service_Bus_Console','Deployer','weblogic.security.principal.WLSGroupImpl','Middleware-App-Deployer')

## Middleware-App-Operator
atnr.createGroup('Middleware-App-Operator','Middleware Application Operator')
appendToRoleExpr('Monitor','|Grp(Middleware#DApp#DOperator)')
appendToRoleExpr('IntegrationMonitor','|Grp(Middleware#DApp#DOperator)')
#grantAppRole('BamServer','BAMContentViewer','weblogic.security.principal.WLSGroupImpl','Middleware-App-Operator')
#grantAppRole('BamServer','IInsightContentViewer','weblogic.security.principal.WLSGroupImpl','Middleware-App-Operator')
grantAppRole('Service_Bus_Console','ApplicationOperator','weblogic.security.principal.WLSGroupImpl','Middleware-App-Operator')

## Middleware-Monitor
atnr.createGroup('Middleware-Monitor','Middleware System Monitor')
appendToRoleExpr('Monitor','|Grp(Middleware#DMonitor)')
appendToRoleExpr('IntegrationMonitor','|Grp(Middleware#DMonitor)')
grantAppRole('soa-infra','SOAMonitor','weblogic.security.principal.WLSGroupImpl','Middleware-Monitor')
#grantAppRole('BamServer','BAMContentViewer','weblogic.security.principal.WLSGroupImpl','Middleware-Monitor')
#grantAppRole('BamServer','IInsightContentViewer','weblogic.security.principal.WLSGroupImpl','Middleware-Monitor')
grantAppRole('Service_Bus_Console','Monitor','weblogic.security.principal.WLSGroupImpl','Middleware-Monitor')

## Middleware-Operator
atnr.createGroup('Middleware-Operator','Middleware System Operator')
grantAppRole('soa-infra','SOAOperator','weblogic.security.principal.WLSGroupImpl','Middleware-Operator')
#grantAppRole('BamServer','BAMContentViewer','weblogic.security.principal.WLSGroupImpl','Middleware-Operator')
#grantAppRole('BamServer','IInsightContentViewer','weblogic.security.principal.WLSGroupImpl','Middleware-Operator')
grantAppRole('Service_Bus_Console','MiddlewareOperator','weblogic.security.principal.WLSGroupImpl','Middleware-Operator')


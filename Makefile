HOST=128.199.73.31
USER=xirc

none:
	exit

deploy:
	cd deploy_tools && fab deploy --host=${USER}@${HOST}

deploy-staging:
	cd deploy_tools && fab deploy --host=${USER}@${HOST} --set=staging=True

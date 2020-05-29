# ec2noip

ec2noip is a Python lambda which update noip.com service when ec2 isntance go up.

## Installation

Install serverless framework.
Then install dependencies.


```bash
npm i -g serverless
npm i
```

Make sure you have enough privileges to deploy this lambda as given in serverless doc https://www.serverless.com/

## Usage
You can update the region in serverless.yml

Deploy this lambda
```bash
sls deploy
```
Configure your lambda environment variables in aws console or with cli.
Go to: https://eu-west-1.console.aws.amazon.com/lambda/home?region=eu-west-1#/functions/ec2noip-dev-start?tab=configuration
Add:
NOIP_USER   your-username-in-nip.com
NOIP_PASS   your-password-in-noip.com
NOIP_DOMAIN the domain you are using in noip.com for example ddns.net

Now once you have a ec2 instance, please tag it with Name=MyFavHost where MyFavHost is an example of hostname you gave noip.com.
Everytime your ec2 machine starts the lambda will call noip REST api and update MyFavHost.ddns.net to the correct IP.

## License
[MIT](https://choosealicense.com/licenses/mit/)
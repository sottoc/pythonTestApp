# pythonTestApp

Commit for verification :)

Site will be similar (in some aspects) to https://mysterybrand.net, so you can refer to it if you have any questions for this test task.

Pick the python framework of you choice (for example Django)
Create initial prototype using python/sql
It should contain following models(db tables):
User (email, pwd) - no confirmation required so far
Account (belongs to user), should have $ amount field (in cents)
Box - item for sale (should have name, price fields)
Transaction account from account to, kind: purchase, deposit, withdraw
Purchase (who bought what)

Admin site allowing basic administration - creating users, depositing funds

Support basic flows/pages:

-Signup (logs you in automatically)
-Login
-Admin adds $ to your account (creates transaction in admin)
-User Profile page shows your balance and purchases.
-List boxes with links to buy.
If you have enough money you can buy box, otherwise error shown -not enough money

send create pull req with your code.
Deploy it on any server so that i can be tested without need to be deployed locally and send me link/credentials
Once submitted I will pick a team of 2-3 best engineers to work on this project.

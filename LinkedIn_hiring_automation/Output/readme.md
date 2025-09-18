#Objective
-
The Objective/Goal was to get the applicants info that have applied to the jobs we have posted on linkedIn, and automate other parts of hiring via API.

#Exploration
-
There are many tools that were explored

The tools mentioned below were not expolred further because they did not provide any free trials without some call or verification procedure

1 Jobvite
2 Job Adder
3 GreenHouse
4 Smart Recruiter
5 Recruitee
6 Smart Pandas

Then I proposed that we can get the applicants linkedIn id, and get their data from there to see if they are a good fit

The Problem with this approach is that we needed more automation, like screening round etc.

I came accross a chrome extention that was for extracting applicants profiles

Resume Exporter for Recruiters

Then I found unipile the tool that met the needs(found on reddit)

#Tools/Flow(Working)
-
The Flow is following if you want to make unipile work in the linkedIn account

##SetUp

1 You need to make a outlook email

2 You need to make a simpleLogin Id using the outlook email and take the email alias from there

3 Using the email alias you need to make LinkedIn and unipile accounts

4 Connect the LinkedIn account to the unipile using LinkedIn credentials

5 Make an API key at unipile to start using it API of linnkedIn

6 Make a .env file and save your important credentials there like, x_api_key, sub_domain and port

Now you can run the codes in the following folder

1 messages
1.1 basic_call.py (To do a basic test call)
1.2 list_all_chats.py (To see the details about chats including id)
1.3 all_attendees_from_chat.py(To see the people involved in chat requires chat id)
1.4 list_of_all_linkedin_accounts.py (To see the list of all linkedIn accounts that are connected with the unipile)
1.5 list_of_all_messages_from_a_chat.py (To get all messages from a chat, required chat id)
1.6 send_message.py (To send a message in your desired chat, requires chat id)

2 users
2.1 list_all_relations.py (Gives the list of all the connects that you have on linkedIn, required unipile account id that can be retrived from basic_call.py)
2.2 list_of_all_invitations_received.py (Gives the list of all the connect requests you have received on linkedIn. Requires unipile account id)
2.3 list_of_all_sent_invitations.py (Gives the list of invitations/connect requests you have sent to people, required unipile account id)

3 linkedin_specific
3.1 list_all_job_posting.py (Will list all the jobs that you have posted)
3.2 perform_linkedIn_search.py (This does a search, but I am not very clear)
3.3 retrive_a_company_profile.py (Retrives the profile of the provided company)
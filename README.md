# Overview:
This is a terminal based application that runs against git repository (local or remote) and uses an LLM
to review the quality of the most recent commit messages. The LLM gives a rating of excellent, good, or bad, and gives a brief
explanation for the rating. This application creates an HTML report, that runs on a simple server hosted on port 3546. The HTML report contains all the ratings the LLM gave as well as the explanation of the rating in an organized manner. The ratings are also available as logs in the terminal as well. This application works for public and private repos on GitHub.

# Important Note:
You do need to create a .env file, this is where you will be storing your API key in an environment variable. 
To get the API Key, go to https://openrouter.ai/openai/gpt-oss-120b:free, and follow the instructions to get the API key.


# Install Instructions:
1. Go to the directory you have saved/downloaded the zip folder
2. If you haven't already done so, unzip the folder
3. Once in the current directory run the command "pip install -e ." (removing the quotation marks)


# Launch Instructions:
1. Assuming you are still in the correct directory, run the command "review_commits" (no quotation marks)

# Testing Instructions:
1. To test this program out all you have to do is step 1 of the Launch Instructions.
2. Once you have done that you can choose either 1 or 2 to select either local repo's or remote repo's
3. If you chose local repo, enter the folder path of the repo that lives on your local machine and press Enter
4. Then watch the terminal to see the LLM output logs directly to the terminal while running 
5. Once the LLM is finished reviewing each commit message, it will generate an html report where you can see the ratings and reasonings for each prompt ordered from most recent to least recent
6. If you chose a remote repo, enter the url of the GitHub repo that you would like to evaluate the commits of, and press Enter
7. Repeat step 4 and 5
8. To stop the local server simply do CTRL + C and it will stop (Sometimes requires you to spam it)"# Commit-Reviwer" 

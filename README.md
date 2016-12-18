# similarity_user_behavior
This project shows similarity in the dictionaries of users_behaviors file

# Goal
1. Create file with this structure
```
[
{
		“userId”: 12345,
	“wordsList”: [“Potato”, “Bacon”, ”Noodles”, “Moon”]
},
{
	“userId”: 46849,
		“wordsList”: [“Insect”, “Bacon”, ”Noodles”, “Boots”]
}
]
```

Jaccard structure:
```
{
 "memberId":{"memberId":"Jaccard_score", "memberId":"Jaccard_score",...,"memberId":"Jaccard_score"}
 "memberId":{"memberId":"Jaccard_score", "memberId":"Jaccard_score",...,"memberId":"Jaccard_score"}
}

example:
{
 "1":{"2":"0.253", "3":"0.023",...,"6532":"0.025"}
 .
 . 
 .
 "6532":{"1":"0.053", "2":"0.013",...,"6532":"1"}
}
```


2. Use jaccard or other method to find similarity in users dictionaries

# How to run

*Please put the steps to run the program or if is a just a code we can run in jupyter*

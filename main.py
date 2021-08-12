import praw
import time

cache = []
reply_text = 'Police report regarding Chris Brown and Rihanna:\n\nChristopher Brown and Robyn F. (Rihanna) have been involved in a dating relationship for approx one and half years. On Sunday, February 8, 2009 at 0025 hours, Brown was driving a vehicle with Robyn F. as the front passenger on an unknown street in Los Angeles. Robin F. picked up Brown’s cellular telephone and observed a three page text message from a woman who Brown had a previous sexual relationship with. A verbal argument ensued and Brown pulled the vehicle over on an unknown street, reached over Robyn F. with his right hand, opened the car door and attempted to force her out. Brown was unable to force Robyn F. out of the vehicle because she was wearing a seat belt. When he could not force her to exit he took his right hand and shoved her head against the passenger window of the vehicle causing an approximate one inch raised circular contusion. Robyn F. turned to face Brown and he punched her in the left eye with his right hand. He then drove away in the vehicle and continued to punch her in the face with his right hand while steering the vehicle with his left hand. The assault caused Robyn F’s mouth to fill with blood and blood to splatter all over her clothing and the interior of the vehicle.\n\nBrown looked at Robyn F. and stated, “I am going to beat the shit out of you when we get home! You wait and see!” Robyn F. picked her cellular telephone and called her personal assistant, Jennifer Rosales at [redacted]. Rosales did not answer the telephone but while her voicemail greeting was playing, Robyn F. pretended to talk to her and stated, “I’m on my way home. Make sure the cops are there when I get there.” (This statement was made while the greeting was playing and was not captured as a message). After Robyn F. faked the call, Brown and looked at her and stated, “You just did the stupidest thing ever! Now I’m really going to kill you.” Brown resumed punching Robyn F. and she interlocked her fingers behind her head and brought her elbows forward to protect her face. She then bent over at the waist, placing her elbows and face near her lap in attempt to protect her face and head from the barrage of punches being levied upon her by Brown. Brown continued to punch Robyn F. on her left arm and hand causing her to suffer a contusion on her left triceps that was approximately two inches in diameter and numerous contusions on her left hand. Robyn F. then attempted to send a text message to her other personal assistant, Melissa Ford. Brown snatched the cellular telephone out of her hand and threw it out of the window onto an unknown street.\n\nBrown continued driving and Robyn F. observed his cellular phone sitting in his lap. She picked up the cellular telephone with her left hand and before she could make a call he placed her in a head lock with his right hand and continued to drive the vehicle with his left hand. Brown pulled Robyn F. close to him and bit her on her left ear. She was able to feel the vehicle swerving from right to left as Brown sped away. He stopped the vehicle in front of [redacted] and Robyn F. turned off the car, removed the key from the ignition and sat on it. Brown did not know what she did with the key and began punching her in the face and arms. He then placed her in a head lock positioning the front of her throat between his bicep and forearm. Brown began applying pressure to Robyn F’s. left and right carotid arteries causing her to be unable to breathe and she began to lose consciousness. She reached up with her left hand and began attempting to gauge his eyes in an attempt to free herself. Brown bit her left ring and middle fingers and then released her. While Brown continued to punch her, she turned around and placed her back against the passenger door. She brought her knees to her chest, placed her feet against Brown’s body and began pushing him away. Brown continued to punch her on the legs and feet causing several contusions. Robyn F. began screaming for help and Brown exited the vehicle and walked away. A resident in the neighborhood heard Robyn F.’s plea for help and called 911, causing a police response. An investigation was conducted and Robyn F. was issued a Domestic Violence Emergency Protective Order (EPO).'

def main():
		reddit = praw.Reddit('bot1')  # imported from praw.ini
		subreddit = reddit.subreddit('all')  # picking subreddit to run on
		print(f'Scan started...')  # logs start
		for comment in subreddit.stream.comments():
		  	process_comment(comment)
		  	time.sleep(2)  # trying to stay under rate limit

def process_comment(comment):
	  normalized_comment = comment.body.lower()  # changing comment to all lowercase
	  if 'ChrisBrownBot' != comment.author:  # do not reply to comments from ourselves
	  		if comment.id not in cache: # do not reply to comments we have already replied to
					  if 'chris brown' in normalized_comment:  # reply only if 'chris brown' is in the comment body
					  		print(f'Replying to: {normalized_comment} by {comment.author}')  # logs replies
					  		cache.append(comment.id)  # adds comment id to cache array
					  		comment.reply(reply_text)  # replies to comment with reply text

if __name__ == '__main__':
    main()

# TODO
# Only reply to first or second level comments

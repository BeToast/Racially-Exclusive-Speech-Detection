This is the github for my final year thesis at University of Galway, Ireland.  
This research was on binary classification of racially/culturally inclusive/exclusive speech using zero-shot and few-shot learning.  
- Slides from my oral presentation: [google slides](https://docs.google.com/presentation/d/13HeoOFVKspvsqmpiliu4R1IgFx8KXomCd52YqrSUCBQ/edit?usp=sharing)

#### Usage
You can access the best performing model on [Huggingface](https://huggingface.co/BeToast/xml_xnli__inclusiveORexclusive__binary_classification__frenchANDenglish)  
or run it in [Google Collab](https://colab.research.google.com/drive/1EABmyXsjQihRS1W9If-weg-lR8i4xn_4?usp=sharing)

#### Abstract
There is an insurmountable amount of negativity on the internet. However, not all of the negativity is deliberate. This paper focuses on detecting racially and culturally exclusive speech with a neutral sentiment. This is preliminary work for an artificial intelligence that can detect exclusive social media posts and then suggest modifications to the post, so the user can easily amend the exclusive post to be inclusive. The solution will not impose on free speech, rather it is an aid to those who desire to improve their speech to be inclusive of all people.  
Promising results have been achieved in detecting exclusivity in French and English language examples using few-shot learning.  More specifically, SetFit, which uses contrastive learning to lessen the distance between sentence embeddings of the same label. This makes generalizing exclusivity much easier due to word embeddings being clustered closer together.

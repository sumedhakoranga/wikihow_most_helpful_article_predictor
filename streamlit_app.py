import pandas as pd
import pickle
import streamlit as st


def prediction(input):
    helpful_percent_prediction = None
    helpful_percent_prediction = percent_helpful_model.predict(input)[0].round(2)

    return helpful_percent_prediction


def main():
    st.title('Wikihow Most Helpful Article Prediction')

    html_temp = """
	<div style ="background-color:yellow;padding:13px">
	<h1 style ="color:black;text-align:center;">Wikihow Most Helpful Article Prediction App </h1>
	</div>
	"""

    st.markdown(html_temp, unsafe_allow_html=True)

    character_count = st.number_input('No. of characters', min_value=None, max_value=None)
    word_count = st.number_input('Total No of Words', min_value=None, max_value=None)
    method_count = st.number_input('The number of methods',min_value=None, max_value=None)
    mean_method_size = st.number_input('The ratio between characters in methods to the method count.', min_value=None, max_value=None)
    mean_paragraph_size = st.number_input('ratio between characters in paragraphs to the paragraph count.',min_value=None, max_value=None)
    size_largest_method = st.number_input('number of characters in the largest method.', min_value=None, max_value=None)
    size_shortest_method = st.number_input('number of characters in the shortest method.', min_value=None, max_value=None)
    std_method_size = st.number_input(
        'standard deviation of the number of characters in methods.', min_value=None, max_value=None)
    step_count = st.number_input('number of steps. ',min_value=None, max_value=None)
    mean_steps_per_method = st.number_input('number of steps divided by the method count.',min_value=None, max_value=None)
    introduction_size = st.number_input(
        'The number of characters in the Introduction.',min_value=None, max_value=None)
    summary_size = st.number_input('The number of characters in summary.',min_value=None, max_value=None)
    references_count = st.number_input('number of references.',min_value=None, max_value=None)
    references_count_per_text_length = st.number_input('number of references divided by the character count.', min_value=None, max_value=None)
    references_count_per_method = st.number_input('number of references divided by the method count.',min_value=None, max_value=None)
    image_count = st.number_input('number of images in an article.', min_value=None, max_value=None)
    image_count_per_method = st.number_input('number of images in an article divided by the method count.',min_value=None, max_value=None)
    num_votes = st.number_input('The number of people who rated the',min_value=None, max_value=None)
    is_expert = st.number_input('an expert author writes the article.', min_value=None, max_value=None)
    views = st.number_input('number of views of the article.',min_value=None, max_value=None)
    co_authors = st.number_input('number of co-authors of', min_value=None, max_value=None)
    warnings = st.number_input('number of warnings in the', min_value=None, max_value=None)
    tips = st.number_input('number of tips in the article.', min_value=None, max_value=None)
    to_be_verb = st.number_input('ratio between the number of “tobe” verbs and the number of words.', min_value=None, max_value=None)
    aux_verb = st.number_input('number of auxiliary verbs.', min_value=None, max_value=None)
    conjunction = st.number_input('number of conjunctions.',min_value=None, max_value=None)
    pronoun = st.number_input('number of pronouns.', min_value=None, max_value=None)
    preposition = st.number_input('number of prepositions.', min_value=None, max_value=None)
    nominalization = st.number_input('number of nominalizations.', min_value=None, max_value=None)
    sentence_beginning_pronoun = st.number_input('number of sentences that start with a pronoun.', min_value=None, max_value=None)
    sentence_beginning_interrogative = st.number_input('number of sentences that start with a sentence_beginning_interrogative.', min_value=None, max_value=None)
    sentence_beginning_article = st.number_input('number of sentences that start with a article.',min_value=None, max_value=None)
    sentence_beginning_subordination = st.number_input('The number of sentences that start with a subordination.', min_value=None, max_value=None)
    sentence_beginning_conjunction = st.number_input('The number of sentences that start with a conjunction.', min_value=None, max_value=None)
    sentence_beginning_preposition = st.number_input('The number of sentences that start with a preposition.', min_value=None, max_value=None)
    Kincaid = st.number_input('Kincaid Grade Level formula,',min_value=None, max_value=None)
    ARI = st.number_input('readability test', min_value=None, max_value=None)
    Coleman_Liau = st.number_input('computes text’s reading complexity', min_value=None, max_value=None)
    FleschReadingEase = st.number_input('FleschReadingEase formula',min_value=None, max_value=None)
    GunningFogIndex = st.number_input('GunningFogIndex', min_value=None, max_value=None)
    LIX = st.number_input('LIX', min_value=None, max_value=None)
    SMOGIndex = st.number_input('SMOGIndex', min_value=None, max_value=None)
    RIX = st.number_input('RIX', min_value=None, max_value=None)
    DaleChallIndex = st.number_input('DaleChallIndex',min_value=None, max_value=None)

    helpful_percent = None
    if st.button('Predict'):
        helful_percent = prediction(
            pd.DataFrame({
                'character_count':character_count, 
                'word_count':word_count, 
                'method_count':method_count, 
                'mean_method_size':mean_method_size,
                'mean_paragraph_size':mean_paragraph_size, 
                'size_largest_method':size_largest_method, 
                'size_shortest_method':size_shortest_method,
                'std_method_size':std_method_size, 
                'step_count':step_count, 
                'mean_steps_per_method':mean_steps_per_method,
                'introduction_size':introduction_size, 
                'summary_size':summary_size, 
                'references_count':references_count,
                'references_count_per_text_length':references_count_per_text_length, 
                'references_count_per_method':references_count_per_method,
                'image_count':image_count, 
                'image_count_per_method':image_count_per_method, 
                'num_votes':num_votes, 
                'is_expert':is_expert,
                'views':views, 
                'co_authors':co_authors, 
                'warnings':warnings, 
                'tips':tips, 
                'to_be_verb':to_be_verb, 
                'aux_verb':aux_verb,
                'conjunction':conjunction, 
                'pronoun':pronoun, 
                'preposition':preposition, 
                'nominalization':nominalization,
                'sentence_beginning_pronoun':sentence_beginning_pronoun, 
                'sentence_beginning_interrogative':sentence_beginning_interrogative,
                'sentence_beginning_article':sentence_beginning_article, 
                'sentence_beginning_subordination':sentence_beginning_subordination,
                'sentence_beginning_conjunction':sentence_beginning_conjunction, 
                'sentence_beginning_preposition':sentence_beginning_preposition,
                'Kincaid':Kincaid, 
                'ARI':ARI, 
                'Coleman_Liau':Coleman_Liau, 
                'FleschReadingEase':FleschReadingEase,
                'GunningFogIndex':GunningFogIndex, 
                'LIX':LIX, 
                'SMOGIndex':SMOGIndex, 
                'RIX':RIX, 
                'DaleChallIndex':DaleChallIndex
            }, index=[0])
        )

        st.success(f'Article is {helpful_percent*100}% helpful')

if __name__ == '__main__':
    with open('percent_helpful_model.pickle', 'rb') as f:
        percent_helpful_model = pickle.load(f)

    main()
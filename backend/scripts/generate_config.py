import os
import textwrap


def main():
    config_content =  textwrap.dedent("""\
    recipe: default.v1 # use Rasa’s default training strategy
    
    language: en # sets English as the language for training data
    
    pipeline: #This section defines the steps involved in the NLU processing
      - name: WhitespaceTokenizer # splits the user's input into individual words based on whitespace
      - name: RegexFeaturizer # this uses regular expressions to extract features from the text
      - name: LexicalSyntacticFeaturizer #extracts features related to the lexical and syntactic structure of the text
      - name: CountVectorsFeaturizer # convert text into a vector representation based on the frequency of words
      - name: CountVectorsFeaturizer # this is another CountVectorsFeaturizer, but configured to use character n-grams
        analyzer: char_wb # specifies that character n-grams within word boundaries should be used
        min_ngram: 1 # set the minimum length of character n-grams to 1
        max_ngram: 4 # set the maximum length of character n-grams to 4
      - name: DIETClassifier # This is a core Rasa component that predicts both the user's intent and extracts entities from the text
        epochs: 100
      - name: EntitySynonymMapper # This component maps extracted entities to their canonical form (e.g., mapping "library" and "lib" to a single "library" entity)
      - name: ResponseSelector #This component selects a predefined response based on the predicted intent and extracted entities
        epochs: 100
      - name: FallbackClassifier #This component determines if the NLU model is not confident in its prediction and triggers a fallback action
        threshold: 0.3
      - name: RegexEntityExtractor
        use_lookup_tables: false
        use_regexes: true
        use_word_boundaries: true
    
    policies: # This section defines how the chatbot decides on its next action in a conversation
      - name: MemoizationPolicy #This policy remembers past conversations and if the current conversation exactly matches a previous one
      - name: RulePolicy #This policy enforces the rules defined in rules.yml, which handle fixed behaviors for specific intents or situations
      - name: UnexpecTEDIntentPolicy #This policy helps the model recover from unexpected user inputs by looking at the last few turns of the conversation
        max_history: 5 #Specifies that the policy will consider the last 5 turns of the conversation
        epochs: 100 # Specifies the number of training iterations for this component
    """)


    with open("./config.yml", "w", encoding="utf-8") as f:
        f.write(config_content)
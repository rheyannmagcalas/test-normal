import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Classifying Online Content to Provide Sustainability Advisory for Small Businesses",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

image = Image.open('logo.jpg')

st.sidebar.image(image,width=250)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


st.sidebar.markdown('<h3 style="color:#1a5276">Classifying Online Content to Provide \
Sustainability Advisory for Small Businesses </h3>', unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "",
    ("Data Sourcing", "Content Classification", "Content Processing", "Project Documentation")
)

if add_selectbox == 'Data Sourcing':
    data_sourcing_filter = st.radio(
     "Data Sourcing Search Type",
     ('Pre-defined format', 'Custom'))

    if data_sourcing_filter == 'Pre-defined format':
        search_word = ''
        col1, col2, col_3 = st.columns(3)
        benefit = col1.text_input('Benefit')
        industry = col2.text_input('Industry')
        country = col_3.selectbox(
        'Country',
        ('Australia', 'Bahrain', 'Brunei', 'Cambodia', 'Colombia', 'Egypt', 'Germany', \
        'India', 'Mexico', 'Pakistan', 'Philippines', 'Thailand', 'United States', 'United Kingdom'))

        if benefit != '' and industry != "":
            search_word = '{} practices in {} industry in {}'.format(benefit, industry, country)
            st.markdown('<b>Search word is: </b> {}'.format(search_word), unsafe_allow_html=True)
    else:
        search_word = st.text_input('Input your search filter here:') 

    if st.button('Search'):
        st.markdown('<h4 style="color:#1a5276">Results: </h4>', unsafe_allow_html=True)

        st.markdown('''<table>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Original URL</th>
                    <th>Clean Dataset</th>
                    <th>Related to Climate Change</th>
                    <th>Industries</th>
                    <th>Countries</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>The Nice Consumer Framework for Achieving Sustainable Fashion Consumption Through Collaboration</td>
                    <td><a href="https://www.bsr.org/reports/nice-consumer-framework.pdf" target="_blank">Original Dataset</a> </td>
                    <td><a href="https://www.bsr.org/reports/nice-consumer-framework.pdf" target="_blank">Cleaned Dataset</a> </td>
                    <td>Yes</td>
                    <td>Fashion</td>
                    <td>United Kingdom</td>
                </tr>
                <tr>
                    <td>SUSTAINABILITY INTEGRATION IN THE FASHION RETAIL INDUSTRY</td>
                    <td><a href="http://www.diva-portal.se/smash/get/diva2:1270877/FULLTEXT01.pdf" target="_blank">Original Dataset</a> </td>
                    <td><a href="http://www.diva-portal.se/smash/get/diva2:1270877/FULLTEXT01.pdf" target="_blank">Cleaned Dataset</a> </td>
                    <td>Yes</td>
                    <td>Fashion, Food</td>
                    <td>United Kingdom, <br> Mexico, <br> Thailand</td>
                </tr>
                <tr>
                    <td>CORPORATE SOCIAL RESPONSIBILITY, THE FINANCIAL SECTOR AND ECONOMIC RECESSION</td>
                    <td><a href="https://www.nottingham.ac.uk/business/who-we-are/centres-and-institutes/gcbfi/documents/researchreports/paper86v2.pdf" target="_blank">Original Dataset</a> </td>
                    <td><a href="https://www.nottingham.ac.uk/business/who-we-are/centres-and-institutes/gcbfi/documents/researchreports/paper86v2.pdf" target="_blank">Cleaned Dataset</a> </td>
                    <td>No</td>
                    <td>Fashion, Tourism</td>
                    <td>United Kingdom, <br> United States, <br> Japan</td>
                </tr>
            </tbody>
        </table>
        ''', unsafe_allow_html=True)

elif add_selectbox == "Content Classification":
    content_classification = st.selectbox(
     "Available Dataset",
     ('The Nice Consumer Framework for Achieving Sustainable Fashion Consumption Through Collaboration', \
      'SUSTAINABILITY INTEGRATION IN THE FASHION RETAIL INDUSTRY'))


    if st.button('See Result'):
        col1, col2 = st.columns(2)
        with col1.expander("Document Information", expanded=True):            
            st.markdown('''<ul>
                <li><b>Title:</b> The Nice Consumer Framework for Achieving Sustainable Fashion Consumption Through Collaboration</li>
                <li><b>Author:</b> n/a</li>
                <li><b>Company:</b> Nordic Fashion Association</li>
                <li><b>Source:</b> https://www.bsr.org/reports/nice-consumer-framework.pdf</li>
                <li><b>File Date Creation:</b> 2021-01-01</li>
                <li><b>Language:</b> 97% English</li>
                <li><b>Related Industries:</b> Fashion, Tourism</li>
                <li><b>Related Countries:</b> United Kingdom</li>
                </ul> ''', unsafe_allow_html=True)

        with col2.expander("Domain Information", expanded=True):
            st.markdown('''<ul>
                <li><b>Domain Authority:</b> 64</li>
                <li><b>Page Authority:</b> 36</li>
                <li><b>Moz Rank:</b> 3.6</li>
                <li><b>Linking Domains:</b> 3</li>
                <li><b>Total Links:</b> 21</li>
                <li><b>Domain Registration Date:</b> 1995-09-03</li>
                <li><b>Domain Updated Date:</b> 2020-03-26</li>
                <li><b>Domain Expiration Date:</b> 2023-09-02</li>
            </ul>''', unsafe_allow_html=True)
            

        with st.expander("Document Summary", expanded=True):            
            st.markdown('The fashion industry can play a leading role to enable sustainable \
                fashion consumption. A number of initiatives exist related \
                to ethical sourcing and production, sustainable design and \
                industry collaboration on product transparency standards. These \
                represent an important foundation for expanded investment in\
                sustainable business models for the fashion industry. ', unsafe_allow_html=True)
        
       
        with st.expander("Extracted Useful Information", expanded=True):            
            st.markdown('''<table>
                <thead>
                    <tr>
                        <th>Summary</th>
                        <th>To Do</th>
                        <th>Supporting Statistics</th>
                        <th>Impact benefit</th>
                        <th>Business Benefit</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Sustainability training and
professional development opportunities</td>
                        <td>Brands and retailers provide sustainability training and
professional development opportunities to their employees,
including designers, sourcing/production, marketing and
advertising staff, and retail store staff</td>
                        <td>Brands and retailers need employees who are
knowledgeable about sustainability and that have the skills
and tools to make decisions that support both financial
success and sustainable consumption and production.</td>
                        <td>Support positive change</td>
                        <td>Increased productivity</td>
                    </tr>
                </tbody>
            </table>
            <br>
            ''', unsafe_allow_html=True)
        with st.expander("Important Keywords", expanded=True):
            st.multiselect(
                'Keywords',
                ['Fashion', 'Sustainability', 'Climate Change', 'Emissions', 'Textile'],
                ['Fashion', 'Sustainability', 'Climate Change', 'Emissions', 'Textile'])

        with st.expander("Mood Analysis", expanded=True):
            col1, col2 = st.columns(2)
            col1.markdown('<h4>Sentiment Analysis </h4>', unsafe_allow_html=True)
            col1.markdown('''<ul>
                <li><b>Positive:</b> 90%</li>
                <li><b>Negative:</b> 5%</li>
                <li><b>Neutral:</b> 10%</li>
                </ul> ''', unsafe_allow_html=True)

            col2.markdown('<h4>Empath Analysis </h4>', unsafe_allow_html=True)
            col2.markdown('''<ul>
                <li><b>Happy:</b> 90%</li>
                <li><b>Angry:</b> 5%</li>
                <li><b>Sad:</b> 10%</li>
                <li><b>Fear:</b> 10%</li>
                </ul><br>''', unsafe_allow_html=True)

            
       
        

        
    





import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics 📊')

new_df = pd.read_csv('datasets/mandar_data_viz1.csv')
feature_text = pickle.load(open('datasets/mandar_feature_text.pkl','rb'))

# this below line gives error, so it is replaced with the 2 lines below that
# group_df = new_df.groupby('sector').mean()[['price','price_per_sqft','built_up_area','latitude','longitude']]
group_df = new_df[['sector','price','price_per_sqft','built_up_area','latitude','longitude']]
group_df = group_df.groupby('sector').mean()[['price','price_per_sqft','built_up_area','latitude','longitude']]
st.header('Sector Price per Sqft Geomap')
st.write('This Geo-map displays the price per square foot across different sectors in the Gurgaon area, color-coded to indicate varying price levels.')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)



# word cloud starts here
# Create a new figure and set dimensions
fig, ax = plt.subplots(figsize=(8, 8))
st.header('Word Cloud')
st.write('This word cloud highlights popular features of properties, such as security, gym, parking, and maintenance.')

# Generate the word cloud
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      stopwords=set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size=10).generate(feature_text)

# Display the generated image:
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")  # Hide axes
# Show the plot in the Streamlit app
st.pyplot(fig)

#  word cloud ends here


# scatter plot starts here
st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])
text = f"This scatter plot explains the trends in Price as the Area increases in {property_type}, and the color-coded points represent the number of bedrooms."
st.write(text)
if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)

# scatter plot ends here



# pie chart starts here
st.header('BHK Pie Chart')
# st.write("This pie chart provides an sector wise BHK distribution with the number of bedrooms.")
st.write("This pie chart provides a sector-wise distribution of properties based on the number of bedrooms (BHK).")

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

    fig2 = px.pie(new_df, names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)
else:

    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

# pie chart ends here



# side by side box plot starts here
st.header('Side by Side BHK price comparison')
st.write('This box plot provides a side-by-side comparison of BHK price distributions, highlighting the price range and outliers for 1BHK, 2BHK, 3BHK, and 4BHK properties in Gurgaon.')
fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)
# side by side box plot ends here



# Side by Side Distplot starts here
st.header('Distplot for Flats vs Houses')
st.write('This shows the comparative price distributions of houses and flats through a distribution plot.')
fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)
# Side by Side Distplot ends here











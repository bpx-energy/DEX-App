import streamlit as st
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns

def main():
        """ Data Explorer App X """
        st.title("D.E.X")
        st.subheadear("Datasets Explorer for BPX Energy")

        def file_selector(C:\\Users\\mark.nations\\Desktop\\Data Explorer\\datasets='.datasets'):
            filenames = os.listdir(C:\\Users\\mark.nations\\Desktop\\Data Explorer\\datasets='.datasets'):)
            selected_filename = st.selectbox("Select a file",filenames)
            return os.path.join(folder_path,selected_filename)

        filename = file_selector()
        st.info("You selected {}".format(filename))

        df = pd.read_csv(filename)

        if st.checkbox("Show Dataset"):
            number = st.number_input("Number of Rows to View")
            st.dataframe(df.head(number))

        if st.button("Column Names"):
            st.write(df.columns)

        if st.checkbox("Shape of Dataset"):
            data_dim = st.radio("Show Dimensions by ",("Rows","Columns"))
            if data_dim == 'Rows':
                st.text("Number of Rows")
                st.write(df.shape[0])
            elif data_dim == 'Columns':
                st.text("Number of Columns")
                st.write(df.shpe[1])
            else:
                st.write(df.shape)

        if st.checkbox("Select Columns to Show"):
            all_columns = df.columns.tolist()
            selected_columns = st.multiselect("Select",all_columns)
            new_df = df[selected_columns]
            st.dataframe(new_df)

        if st.button("Value Count"):
            st.text("Value Counts by Target/Class")
            st.write(df.iloc[:,-1].value_counts())

        if st.button("Data Types"):
            st.write(df.types)

        if st.checkbox("Summary"):
            st.write(df.describe().T)

        st.subheader("Data Visualization")

        if st.checkbox("Correlation Plot[Seaborn]"):
            st.write(sns.heatmap(df.corr(),annot=True))
            st.pyplot()

        if st.checkbox("Pie Plot"):
            all_columns_names = df.columns.tolist()
            if st.button("Generate Pie Plot"):
                st.success("Generating A Pie Plot")
                st.write(df.iloc[:-1].value_counts().plot.pie(autopct="%1.1f%%"))
                st.pyplot()

        if st.checkbox("Plot of Value Counts"):
            st.text("Value Counts by Target")
            all_columns_names = df.columns.tolist()
            primary_col = st.selectbox("Primary Column to GroupBy",all_columns_names)
            selected_columns_names = st.multiselect("Select Columns",all_columns_names)
            if st.button("Plot"):
                st.text("Generate Plot")
                if selected_columns_names:
                    vc_plot = df.groupby(primary_col)[selected_columns_names].count()
                else:
                    vc_plot = df.iloc[:,-1].value_counts()
                st.write(vc_plot.plot(kind="bar"))
                st.pyplot()

        # Customizable plot

        st.subheader("Customizable Plot")
        all_columns_names = df.columns.tolist()
        type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
        selected_columns_names = st.multiselect("Select Columns to Plot",all_columns_names)

        if st.button("Generate Plot"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

                    # Plot by streamlit
                    if type_of_plot == 'area':
                        cust_data = df[selected_columns_names]
                        st.area_chart(cust_data)

                    elif type_of_plot == 'bar':
                        cust_data = df[selected_columns_names]
                        st.bar_chart(cust_data)

                    elif type_of_plot == 'line':
                        cust_data = df[selected_columns_names]
                        st.line_chart(cust_data)

                    # Custom plot
                    elif type_of_plot:
                        cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
                        st.write(cust_plot)
                        st.pyplot()

        if st.button("Travis Comer Rocks!"):
                    st.baloons()

        # Sidebar (Left Gutter)
        st.sidebar.header("About App")
	    st.sidebar.info("A pythonic App for Exploring BPX Energy Datasets")

	    st.sidebar.header("Get Datasets")

	    st.sidebar.header("About")
	    st.sidebar.info("App for exploring various datasets")
	    st.sidebar.text("Built with Streamlit")
	    st.sidebar.text("Authored by mark.nations@bpx.com")


if __name__ == '__main__':
	main()


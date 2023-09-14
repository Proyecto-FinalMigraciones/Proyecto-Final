import streamlit as st
import joblib
import numpy as np



model = joblib.load('modelo_migracion.pkl')

st.image('logo.png', width=300)
st.title('Predicción de Flujos Migratorios')

# Describe los pasos
st.markdown('### Ingreso de datos')
st.write('Complete los campos de entradaen los siguentes campos.')

# Añade elementos de entrada para las características necesarias para hacer predicciones
option = st.selectbox(
    'País',
    ("Argentina", "Australia", "Brazil", "China", "France", "Germany", "India", "Indonesia", "Italy", "Japan", "Korea, Rep.", "Mexico",
     "Netherlands", "Russian Federation", "Saudi Arabia", "Spain", "Switzerland", "Turkiye", "United Kingdom", "United States","Afghanistan",
     "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Antigua and Barbuda", "Armenia", "Aruba", "Austria", "Azerbaijan", "Bahamas, The",
     "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bhutan", "Bolivia", "Bosnia and Herzegovina",
     "Botswana", "British Virgin Islands", "Brunei Darussalam", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
     "Canada", "Cayman Islands", "Central African Republic", "Chad", "Channel Islands", "Chile", "Colombia", "Comoros", "Congo, Dem. Rep.",
     "Congo, Rep.", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Curacao", "Cyprus", "Czechia", "Denmark", "Djibouti", "Dominica",
     "Dominican Republic", "Ecuador", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Egypt, Arab Rep.", "Eswatini", "Ethiopia",
     "Faroe Islands", "Fiji", "Finland", "French Polynesia", "Gabon", "Gambia, The", "Georgia", "Ghana", "Gibraltar", "Greece", "Greenland",
     "Grenada", "Guam", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hong Kong SAR, China", "Hungary", "Iceland",
     "Iran, Islamic Rep.", "Iraq", "Ireland", "Isle of Man", "Israel", "Jamaica", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, Dem. People's Rep.",
     "Kosovo", "Kuwait", "Kyrgyz Republic", "Lao PDR", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg",
     "Macao SAR, China", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Micronesia, Fed. Sts.",
     "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "New Caledonia", "New Zealand",
     "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Northern Mariana Islands", "Norway", "Oman", "Pakistan", "Palau","Panama", "Papua New Guinea",
     "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar"))
st.write('Ingrese el nombre del país para la predicción', option)


feature1 = st.number_input('Muertes por conflicto', step=1)
st.write('Ingrese el número de muertes por conflicto')

feature2 = st.number_input('Control de corrupción')
st.write('Ingrese el nivel de control de corrupción')

feature3 = st.slider('Crecimiento PIB (%)', min_value=0.0, max_value=20.0)
st.write('Ingrese el crecimiento del PIB en porcentaje')

feature4 = st.slider('Tasa desempleo (%)', min_value=0.0, max_value=30.0)
st.write('Ingrese la tasa de desempleo en porcentaje')



st.markdown('### Realice la predicción')
st.write('Haga clic en el botón "Realizar Predicción" para obtener el resultado.')
# Agrega un botón para realizar la predicción cuando el usuario lo presiona
if st.button('Realizar Predicción'):
      # Verifica si todos los campos están completos antes de realizar la predicción
    if option and feature1 is not None and feature2 is not None and feature3 is not None and feature4 is not None:
        # Realiza la predicción utilizando el modelo
        features = np.array([feature1, feature2, feature3, feature4]).reshape(1, -1)
        prediction = model.predict(features)
        prediction = int(round(prediction[0]))
        st.write(f'Predicción: {prediction}')
    else:
        st.warning('Por favor complete todos los campos antes de realizar la predicción.')    


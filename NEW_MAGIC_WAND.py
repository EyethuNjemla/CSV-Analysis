 
#TEAM NEW MAGIC WAND
'''
TEAM MEMBERS: EYETHU, MOLOTI, GUGULETHU, PEACE,
             DRESHAAN, BENEDICT
'''
import re
from collections import defaultdict, Counter

def main():
    #file location comes here
    file_path = "C:\\Users\\melod\\Downloads\\thetext.txt"
    
    #data structure mainly dictionary
    countries_ending_a = []
    city_populations = {}
    country_landmass = {}
    indep_1960_1980 = []
    indep_1830_1850 = []
    african_countries_life_exp = {}
    all_languages = []
    countries_ending_a_unique = set()
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:

            headers = file.readline().strip().split(",")  # Read header
            language_index = headers.index("Language")   # Get correct column index for Language
            life_exp_index = headers.index("LifeExpectancy")  # Correct index for life expectancy
        
            for line_num, line in enumerate(file):
                if line_num == 0:
                    #check first line (for header)
                    if any(word in line.lower() for word in ['city', 'country', 'population', 'landmass']):
                        continue
                #split the line by a comma
                values = [val.strip() for val in line.strip().split(",")]
                
                #Do we have enough columns?well let's make sure
                if len(values) < 15:
                    continue
                
                #EXTRACT die DATA
                city_name = values[0] if len(values) > 0 else ""
                city_pop_str = values[1] if len(values) > 1 else ""
                country = values[2] if len(values) > 2 else ""
                continent = values[3] if len(values) > 3 else ""
                landmass_str = values[5] if len(values) > 5 else ""
                life_exp_str = values[life_exp_index] if len(values) > life_exp_index else ""
                indep_year_str = values[6] if len(values) > 6 else ""
                lang1 = values[7] if len(values) > 7 else ""
                lang2 = values[8] if len(values) > 8 else ""
                lang3 = values[9] if len(values) > 9 else ""
                
                
                #Peace: Question A: Count ending with 'a'
                if country and country.lower().endswith('a'):
                    countries_ending_a.append(country)
                    countries_ending_a_unique.add(country)
                    
                #Moloti: Question B: City populations(descending order)
                if city_name and city_pop_str:
                    try:
                        #Remove commas and convert to int
                        city_pop = int(city_pop_str.replace(",", "").replace("", ""))
                        if city_pop > 0:
                            if city_name in city_populations:
                                city_populations[city_name] = max(city_populations[city_name], city_pop)
                            else:
                                city_populations[city_name] = city_pop
                    except ValueError:
                        pass
                    
                #Gugulethu: Question C: Country landmass
                if country and landmass_str:
                    try:
                        landmass = float(landmass_str.replace(",", "").replace("", ""))
                        if landmass > 0:
                            if country in country_landmass:
                                country_landmass[country] = max (country_landmass[country], landmass)
                            else:
                                country_landmass[country] = landmass
                                
                    except ValueError:
                        pass
                    
                #Eyethu: Question D: Independence 1960-1980
                if indep_year_str and indep_year_str.isdigit():
                    year = int(indep_year_str)
                    if 1960 <= year <= 1980:
                        if country and country not in indep_1960_1980:
                            indep_1960_1980.append(country)
                        
                        
                #Bennedict: Question E: Independence 1830-1850
                if indep_year_str and indep_year_str.isdigit():
                    year = int(indep_year_str)
                    if 1830 <= year <= 1850:
                        if country not in indep_1830_1850:
                            indep_1830_1850.append(country)
                            
                #Dreshaan: Question F: African countries life expectancy
                if continent and continent.lower().strip() == 'africa' and life_exp_str:
                    try:
                        life_exp = float(life_exp_str.replace(",", "").replace("", ""))
                        if life_exp > 0:
                            if country in african_countries_life_exp:
                                african_countries_life_exp[country] = max(african_countries_life_exp[country], life_exp)
                            else:
                                african_countries_life_exp[country] = life_exp
                    except ValueError:
                        pass
                    
                #Eyethu: Question G: Languages
                '''for lang in [lang1, lang2,  lang3]:
                    if lang and lang.strip() and lang.lower() not in ['', 'none', 'n/a']:
                        #check if it's not a number
                        if not lang.replace('.', '').replace(',', '').isdigit():
                            all
                        #all_languages.append(lang.strip())'''
                
                if len(values) > language_index:
                    language = values[language_index].strip()
                    if language.lower() not in ["", "none", "n/a"]:
                        all_languages.append(language)
                        
                        
                        
                #Write to a text file named file2.text
            write_results_to_file(
                    len(countries_ending_a),
                    city_populations,
                    country_landmass,
                    indep_1960_1980,
                    indep_1830_1850,
                    african_countries_life_exp,
                    all_languages,
                    countries_ending_a_unique
            )
                
                
            print("Analysis complete!! Results written to file2.txt")
                
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and path.")
    except UnicodeDecodeError:
        print("Error: Could not decode the file. Please check the file encoding format.")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
def write_results_to_file(count_a, city_pops, country_land, list_d, list_e, african_life, languages, unique_countries_a):
    """Write all results to the text file"""
    
    try:
        with open("file2.txt", "w", encoding = "utf-8") as output_file:
            
            #Question A
            output_file.write("Question a:\n")
            output_file.write(f"Number of country names ending with 'a': {count_a}\n\n")
            
            #Question B
            output_file.write("Question b:\n")
            if city_pops:
                top_5_cities = sorted(city_pops.items(), key=lambda x: x[1], reverse=True)[:5]
                output_file.write("Top 5 cities by population:\n")
                for i, (city, population) in enumerate(top_5_cities, 1):
                    output_file.write(f"{i}. {city}: {population:,}\n")
            else:
                output_file.write("No city population data found.\n")
            output_file.write("\n")
            
            #Question C
            
            output_file.write("Question c:\n")
            if country_land:
                top_5_landmass = sorted(country_land.items(), key = lambda x: x[1], reverse=True)[:5]
                output_file.write("Top 5 countries by landmass:\n")
                for i, (country, landmass) in enumerate(top_5_landmass, 1):
                    output_file.write(f"{i}.{country}:{landmass:,.2f}\n")
            else:
                output_file.write("No landmass data found.\n")
            output_file.write("\n")
            
            
            #Question D
            output_file.write("Question D:\n")
            output_file.write(f"Number of countries that gained independence between 1960-1980: {len(list_d)}\n\n")
            if list_d:
                output_file.write("Countries that gained independence between 1960-1980:\n")
                for country in sorted(list_d):
                    output_file.write(f"- {country}\n")
            output_file.write("\n")
            
            #Question E
            output_file.write("Question E:\n")
            if list_e:
                output_file.write("Countries that gained independence between 1830-1850:\n")
                for country in list_e:
                    output_file.write(f"-{country}\n")
                    
            else:
                output_file.write("No countries found that gained independence between 1830-1850.\n")
            output_file.write("\n")
            
            #Question F
            output_file.write("Question f:\n")
            if african_life:
                top_5_african = sorted(african_life.items(), key=lambda x: x[1], reverse=True)[:5]
                output_file.write("Top 5 African countries by life expectancy:\n")
                for i, (country, life_exp) in enumerate(top_5_african, 1):
                    output_file.write(f"{i}. {country}: {life_exp:.1f} years\n")
                else:
                    output_file.write("Life expectancy.\n")
                output_file.write("\n")
                
                
            #Question G
            output_file.write("Question g:\n")
            if languages:
                languages_counts = Counter(languages)
                top_5_languages = languages_counts.most_common(5)
                output_file.write("Top 5 most commonly spoken languages:\n")
                for i, (language, count) in enumerate(top_5_languages, 1):
                    output_file.write(f"{i}.{language}: {count} occurrences\n")
            else:
                output_file.write("No languages data found.\n")
            output_file.write("\n")
            
            #Question H
            output_file.write("Question H:\n")
            if unique_countries_a:
                output_file.write("Unique country names ending with 'a':\n")
                for country in sorted(unique_countries_a):
                    output_file.write(f"-{country}\n")
            else:
                output_file.write("No unique countries ending with 'a':\n")
            output_file.write("\n")
            
        print("Results successfully written to file2.txt")
        
    except Exception as e:
        print(f"Error writing to file: {e}")
        
        
def print_results_to_console(count_a, city_pops, country_land, list_d, list_e, african_life, languages, unique_countries_a):
    """Results to console vie"""
    print(f"\nQuestionA: {count_a} countries end with 'a'")
    
    if city_pops:
        top_5_cities = sorted(city_pops.items(), key=lambda x: x[1], reverse=True)[:5]
        print(f"\nQuestion B: Top 5 cities by population:")
        for i, (city, pop) in enumerate (top_5_cities, 1):
            print(f"{i}. {city}: {pop:,}")
            
    if country_land:
        top_5_landmass = sorted(country_land.items(), key = lambda x: x[1], reverse=True)[:5]
        print(f"\nQuestion C: Top 5 countries by landmass:")
        for i, (country, landmass) in enumerate(top_5_landmass, 1):
            print(f"{i}.{country}:{landmass:,.2f}")
            
    print(f"\nQuestion D: {list_d} countries gained independence between 1960-1980")
    
    if list_e:
        print(f"\nQuestion E: Countries independent between 1830-1850:")
        for country in list_e:
            print(f"-{country}")
            
if __name__ == "__main__":
    main()
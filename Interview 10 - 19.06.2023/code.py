def flatten_dictionary(dictionary):
    output = dict()

    def recursion(temp_key, dict_temp):

        for key in dict_temp:

            if type(dict_temp[key]) != dict:
                if temp_key != "":
                    output[(temp_key + '.' + key).strip('.')] = dict_temp[key]
                else:
                    output[key] = dict_temp[key]
            else:
                if temp_key != "":
                    recursion(temp_key + "." + key, dict_temp[key])
                else:
                    recursion(key, dict_temp[key])

    recursion('', dictionary)
    return output
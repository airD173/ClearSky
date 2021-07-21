import discord
import icon

def main(data1, data2):
    #Data is (zipcode, name, temp, icon, short, detailed)
    f1 = str(data1[2]) + '°F'
    f2 = str(data2[2]) + '°F'
    c1 =(data1[2] - 32) * 5 / 9
    c1 = str(round(c1, 1)) + '°C'
    c2 =(data2[2] - 32) * 5 / 9
    c2 = str(round(c2, 1)) + '°C'

    embedf1 = discord.Embed(title = data1[0], description = None, color = 0xFFAC33)
    if data1[3] == None:
        pass
    else:
        embedf1.set_thumbnail(url = data1[3])
    embedf1.add_field(name = data1[1], value = f1 + '\n' + data1[4], inline = False)
    embedf1.add_field(name = data2[1], value = f2 + '\n' + data2[4], inline = False)
    embedf1.set_footer(text = 'Page 1 of 3\nCreated by airD')

    embedf2 = discord.Embed(title = data1[0], description = data1[1], color = 0xFFAC33)
    if data1[3] == None:
        pass
    else:
        embedf2.set_thumbnail(url = data1[3])
    embedf2.add_field(name = 'Temperature', value = f1, inline = False)
    embedf2.add_field(name = 'Weather', value = data1[5], inline = False)
    embedf2.set_footer(text = 'Page 2 of 3\nCreated by airD')

    embedf3 = discord.Embed(title = data2[0], description = data2[1], color = 0xFFAC33)
    if data2[3] == None:
        pass
    else:
        embedf3.set_thumbnail(url = data2[3])
    embedf3.add_field(name = 'Temperature', value = f2, inline = False)
    embedf3.add_field(name = 'Weather', value = data2[5], inline = False)
    embedf3.set_footer(text = 'Page 3 of 3\nCreated by airD')

    embedc1 = discord.Embed(title = data1[0], description = None, color = 0xFFAC33)
    if data1[3] == None:
        pass
    else:
        embedc1.set_thumbnail(url = data1[3])
    embedc1.add_field(name = data1[1], value = c1 + '\n' + data1[4], inline = False)
    embedc1.add_field(name = data2[1], value = c2 + '\n' + data2[4], inline = False)
    embedc1.set_footer(text = 'Page 1 of 3\nCreated by airD')

    embedc2 = discord.Embed(title = data1[0], description = data1[1], color = 0xFFAC33)
    if data1[3] == None:
        pass
    else:
        embedc2.set_thumbnail(url = data1[3])
    embedc2.add_field(name = 'Temperature', value = c1, inline = False)
    embedc2.add_field(name = 'Weather', value = data1[5], inline = False)
    embedc2.set_footer(text = 'Page 2 of 3\nCreated by airD')

    embedc3 = discord.Embed(title = data2[0], description = data2[1], color = 0xFFAC33)
    if data2[3] == None:
        pass
    else:
        embedc3.set_thumbnail(url = data2[3])
    embedc3.add_field(name = 'Temperature', value = c2, inline = False)
    embedc3.add_field(name = 'Weather', value = data2[5], inline = False)
    embedc3.set_footer(text = 'Page 3 of 3\nCreated by airD')   
    
    return((embedf1, embedf2, embedf3, embedc1, embedc2, embedc3))
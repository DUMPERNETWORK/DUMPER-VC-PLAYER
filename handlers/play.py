try:
        chatdetails = await USER.get_chat(chid)
        #lmoa = await client.get_chat_member(chid,wew)
    except:
        await lel.edit(
            f"<i> {user.first_name} Userbot not in this chat, Ask admin to send /play command for first time or add {user.first_name} manually</i>"
        )
        return     
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name
    await lel.edit("**__Searching Your Song__**")
    sender_id = message.from_user.id
    user_id = message.from_user.id
    sender_name = message.from_user.first_name
    user_name = message.from_user.first_name
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    await lel.edit("**__Processing Your Song__**")
    ydl_opts = {"format": "bestaudio/best"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        url = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        await lel.edit("Song not found.Try another song or maybe spell it properly.")
        print(str(e))
        return

    keyboard = InlineKeyboardMarkup(
            [   
                [
                               
                    InlineKeyboardButton('📖 Playlist', callback_data='playlist'),
                    InlineKeyboardButton('Menu ⏯ ', callback_data='menu')
                
                ],                     
                [
                    InlineKeyboardButton('YouTube 🎬', url=f'{url}'),
                    InlineKeyboardButton('Close 🗑', callback_data='cls')
                
                ]                             
            ]
        )
    requested_by = message.from_user.first_name
    await generate_cover(requested_by, title, views, duration, thumbnail)  
    file_path = await converter.convert(youtube.download(url))
  
    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        qeue = que.get(message.chat.id)
        s_name = title
        r_by = message.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        await message.reply_photo(
        photo="final.png", 
        caption=f"#⃣ Your requested song queued at position {position}!",
        reply_markup=keyboard,
        )
        os.remove("final.png")
        return await lel.delete()
    else:
        chat_id = message.chat.id
        que[chat_id] = []
        qeue = que.get(message.chat.id)
        s_name = title            
        r_by = message.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]      
        qeue.append(appendable)
        try:
            callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        except:
            message.reply("Group Call is not connected or I can't join it")
            return
        await message.reply_photo(
        photo="final.png",
        reply_markup=keyboard,
        caption="▶️ Playing Here The Song Requested By {}".format(
        message.from_user.mention()
        ),
    )
    os.remove("final.png")
    return await lel.delete()

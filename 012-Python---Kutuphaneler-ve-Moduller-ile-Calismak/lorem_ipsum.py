# Bizim Kutuphanemiz :)

def lorem_generator(word_count=1):
    txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis faucibus feugiat augue ac viverra. Suspendisse potenti. Donec porta et tortor at porttitor. Cras gravida varius velit et porta. Etiam aliquam, metus et vestibulum aliquam, odio lacus condimentum ante, vitae ultrices justo ex eu augue. Proin venenatis quam vitae condimentum finibus. Cras lorem magna, tempus vitae enim quis, tincidunt placerat lorem. Suspendisse leo odio, tincidunt eget arcu non, dictum maximus lorem. Donec eros mi, dignissim in sodales id, rhoncus vel nulla. Praesent varius neque arcu, sagittis congue velit ultrices non. Nunc elementum, turpis eget auctor euismod, tellus massa sollicitudin lacus, a posuere orci lectus nec ligula. Sed faucibus consequat feugiat. Mauris sed vehicula sapien, ut interdum ligula. Donec nec augue eu felis luctus finibus at feugiat eros. Mauris commodo libero enim, id dignissim magna auctor a. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam id luctus tellus, eu mattis odio. Nam eu gravida mauris, sit amet molestie sem. Pellentesque auctor urna sed pretium eleifend. Aliquam erat volutpat. Cras bibendum sem nibh, eget rutrum nisl vehicula id. Etiam semper ante vel ipsum finibus, sit amet facilisis enim sollicitudin. Ut id diam elementum, accumsan arcu in, posuere massa. Aliquam nulla ipsum, efficitur at neque sit amet, mollis vestibulum dui."

    txt_arr = txt.split(" ") # text yapiyi array olarak cevirdim.
    lorem_words = " ".join(txt_arr[:word_count])
    return lorem_words
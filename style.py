style_main = """
    QMainWindow {
        background-color: rgb(42, 39, 46);
        color: white;
    }
    
    QLabel {
        color: white;
    }
    
    QListWidget{
        background-color: rgb(42, 39, 46);
        color: white;
        border: 2px solid rgb(255, 176, 178);
    }

    QSlider::groove:horizontal {
        background: rgb(255, 176, 178);
        position: absolute;
        left: 4px;
        right: 4px;
    }

    QSlider::handle:horizontal {
        height: 10px;
        background: rgb(64, 59, 70);
        margin: 0 -4px;
    }

    QSlider::add-page:horizontal {
        background: white;
    }

    QSlider::sub-page:horizontal {
        background: rgb(255, 176, 178);
    }
"""

style_play_btn = """
    border-radius: 40px;
    background-color: rgb(255, 176, 178);
"""

style_prev_next_btn = """
    background-color: rgb(64, 59, 70);
    border-radius: 20px;
"""

style_choose_btn = """
    color: white;
    border: 2px solid rgb(255, 176, 178);
"""
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from PIL import Image, ImageTk
import calendar
from datetime import datetime, timedelta
from tkcalendar import Calendar

class PostingInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Posting Interface")
        
        # Set dark theme colors
        self.colors = {
            "bg": "#151517",
            "fg": "#ffffff",
            "button": "#1890ff",
            "border": "#26262A",
            "sidebar": "#101010",
            "hover": "#26262A",
            "text_bg": "#1E1E1E"
        }
        
        self.root.configure(bg=self.colors["bg"])
        
        # Create main layout
        self.create_navbar()
        self.create_main_layout()
        
    def create_navbar(self):
        # Top navbar
        self.navbar = tk.Frame(
            self.root,
            bg=self.colors["sidebar"],
            height=60
        )
        self.navbar.pack(fill=tk.X, side=tk.TOP)
        
        # Logo
        logo_label = tk.Label(
            self.navbar,
            text="HP",
            fg=self.colors["fg"],
            bg=self.colors["sidebar"],
            font=("Helvetica", 20, "bold")
        )
        logo_label.pack(side=tk.LEFT, padx=20)
        
        # Left side navigation buttons
        nav_buttons = {
            "Post": self.show_post_content,
            "Schedules": self.show_schedule_content,
            "MonoLink": lambda: None  # Placeholder for MonoLink
        }
        
        for btn_text, command in nav_buttons.items():
            btn = tk.Button(
                self.navbar,
                text=btn_text,
                bg=self.colors["sidebar"],
                fg=self.colors["fg"],
                relief=tk.FLAT,
                padx=15,
                activebackground=self.colors["hover"],
                command=command
            )
            btn.pack(side=tk.LEFT, padx=5)

        # Right side buttons
        right_buttons = ["README", "Platform Algorithms"]
        for btn_text in right_buttons:
            btn = tk.Button(
                self.navbar,
                text=btn_text,
                bg=self.colors["sidebar"],
                fg=self.colors["fg"],
                relief=tk.FLAT,
                padx=15,
                activebackground=self.colors["hover"],
                command=lambda x=btn_text: self.show_info_window(x)
            )
            btn.pack(side=tk.RIGHT, padx=5)

    def show_info_window(self, window_type):
        info_window = tk.Toplevel(self.root)
        info_window.configure(bg=self.colors["bg"])
        info_window.geometry("800x600")
        
        if window_type == "README":
            info_window.title("README - Usage Guide")
            self.create_readme_content(info_window)
        else:
            info_window.title("Platform Algorithms Guide")
            self.create_algorithm_content(info_window)

    def create_readme_content(self, window):
        readme_text = """
# Social Media Posting Interface

## Overview
This application allows you to manage and schedule posts across multiple social media platforms.

## Features
- Multi-platform posting
- Media upload support
- Post scheduling
- Preview functionality
- Platform-specific settings

## Usage
1. Select your target platforms
2. Upload media content
3. Write your post
4. Configure platform-specific settings
5. Preview your post
6. Schedule or publish immediately

## Support
For additional support, please contact support@example.com
        """
        
        text_widget = scrolledtext.ScrolledText(
            window,
            bg=self.colors["text_bg"],
            fg=self.colors["fg"],
            font=("Courier", 10),
            padx=10,
            pady=10
        )
        text_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        text_widget.insert(tk.END, readme_text)
        text_widget.configure(state='disabled')

    def create_algorithm_content(self, window):
        window.configure(bg="#151517")
        
        # Style configuration for the notebook
        style = ttk.Style()
        style.theme_create("dark", parent="alt", settings={
            "TNotebook": {
                "configure": {
                    "background": "#151517",
                    "tabmargins": [2, 5, 2, 0],
                    "padding": [10, 5]
                }
            },
            "TNotebook.Tab": {
                "configure": {
                    "background": "#1E1E1E",
                    "foreground": "#FFFFFF",
                    "padding": [15, 5],
                    "font": ('Helvetica', 10)
                },
                "map": {
                    "background": [("selected", "#1890ff")],
                    "foreground": [("selected", "#FFFFFF")],
                    "expand": [("selected", [1, 1, 1, 0])]
                }
            },
            "TFrame": {
                "configure": {
                    "background": "#151517"
                }
            }
        })
        style.theme_use("dark")

        # Create notebook with custom style
        notebook = ttk.Notebook(window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Platform tabs configuration
        platforms = {
            "TikTok": {"color": "#000000", "text": "#FFFFFF"},
            "Instagram": {"color": "#1E1E1E", "text": "#FFFFFF"},
            "LinkedIn": {"color": "#1E1E1E", "text": "#FFFFFF"},
            "YouTube": {"color": "#1E1E1E", "text": "#FFFFFF"},
            "Pinterest": {"color": "#1E1E1E", "text": "#FFFFFF"},
            "Snapchat": {"color": "#1E1E1E", "text": "#FFFFFF"},
            "RedNote": {"color": "#1E1E1E", "text": "#FFFFFF"},
            "Lemon8": {"color": "#1E1E1E", "text": "#FFFFFF"}
        }

        # Create tabs for each platform
        for platform, colors in platforms.items():
            frame = ttk.Frame(notebook)
            notebook.add(frame, text=platform)
            
            text_widget = scrolledtext.ScrolledText(
                frame,
                bg="#1E1E1E",
                fg="#FFFFFF",
                font=("Helvetica", 11),
                padx=20,
                pady=20,
                insertbackground="#FFFFFF",  # Cursor color
                selectbackground="#1890ff",  # Selection background
                selectforeground="#FFFFFF",  # Selection text color
                borderwidth=0,
                highlightthickness=0
            )
            text_widget.pack(fill=tk.BOTH, expand=True)
            
            # Add custom tags for formatting
            text_widget.tag_configure("heading1", 
                font=("Helvetica", 16, "bold"), 
                foreground="#1890ff"
            )
            text_widget.tag_configure("heading2", 
                font=("Helvetica", 14, "bold"),
                foreground="#FFFFFF"
            )
            text_widget.tag_configure("bullet", 
                font=("Helvetica", 11),
                foreground="#CCCCCC"
            )
            
            # Insert content with formatting
            content = self.get_platform_content(platform)
            text_widget.insert(tk.END, content)
            
            # Apply formatting to headings and bullets
            text_widget.tag_add("heading1", "1.0", "1.end")
            
            # Make text read-only
            text_widget.configure(state='disabled')

    def get_platform_content(self, platform):
        # Platform-specific content remains the same as before
        platform_content = {
            "TikTok": """
# TikTok Algorithm Guide

## Key Factors
• Watch Time: The longer viewers watch, the better
• Completion Rate: Videos watched from start to finish
• User Interactions: Likes, comments, shares, follows
• Hashtag Relevance: Using trending and niche hashtags
• Sound Usage: Trending sounds boost visibility

## Best Practices
1. Hook viewers in first 3 seconds
2. Keep videos between 21-34 seconds for optimal completion
3. Post 1-4 times per day
4. Use trending sounds and effects
5. Engage with comments within first hour

## Optimal Post Times
• Weekdays: 6-9 AM, 11 AM-2 PM, 7-10 PM EST
• Weekends: 11 AM-7 PM EST
• Peak engagement: Tuesday-Thursday

## Content Strategy
• Follow trends but add unique twist
• Use pattern interrupts
• Create series content
• Maintain consistent posting schedule
• Cross-promote on other platforms
""",
            # ... (other platform content remains the same)
        }
        return platform_content.get(platform, "Content not available for this platform.")

    def create_main_layout(self):
        # Main container with sidebar and content
        self.main_container = tk.Frame(
            self.root,
            bg=self.colors["bg"]
        )
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Create sidebar
        self.create_sidebar()
        
        # Create content area
        self.content_area = tk.Frame(
            self.main_container,
            bg=self.colors["bg"]
        )
        self.content_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create different content frames
        self.post_content = self.create_post_content()
        self.schedule_content = self.create_schedule_content()
        
        # Initially show post content
        self.show_post_content()

    def create_sidebar(self):
        # Sidebar frame
        self.sidebar = tk.Frame(
            self.main_container,
            bg=self.colors["sidebar"],
            width=200
        )
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.sidebar.pack_propagate(False)
        
        # Platform buttons
        platforms = [
            "Facebook", "Twitter", "Instagram", "LinkedIn",
            "TikTok", "YouTube", "Pinterest", "Snapchat",
            "RedNote", "Lemon8"
        ]
        
        for platform in platforms:
            btn = tk.Button(
                self.sidebar,
                text=platform,
                bg=self.colors["sidebar"],
                fg=self.colors["fg"],
                relief=tk.FLAT,
                padx=20,
                pady=10,
                anchor="w",
                width=20,
                activebackground=self.colors["hover"]
            )
            btn.pack(fill=tk.X, padx=5, pady=2)

    def create_post_content(self):
        # Post content area
        post_frame = tk.Frame(
            self.content_area,
            bg=self.colors["bg"]
        )
        post_frame.pack(fill=tk.BOTH, expand=True, pady=20)
        
        # Media upload area
        upload_frame = tk.LabelFrame(
            post_frame,
            text="Upload Media",
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        upload_frame.pack(fill=tk.X, pady=10)
        
        upload_btn = tk.Button(
            upload_frame,
            text="+ Upload Media",
            command=self.upload_media,
            bg=self.colors["button"],
            fg=self.colors["fg"]
        )
        upload_btn.pack(pady=20)
        
        # Post content area
        content_frame = tk.LabelFrame(
            post_frame,
            text="Post Content",
            bg=self.colors["bg"],
            fg=self.colors["fg"]
        )
        content_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.content_text = tk.Text(
            content_frame,
            bg=self.colors["border"],
            fg=self.colors["fg"],
            height=10
        )
        self.content_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Settings
        settings_frame = tk.LabelFrame(
            post_frame,
            text="Settings",
            bg=self.colors["bg"],
            fg=self.colors["fg"]
        )
        settings_frame.pack(fill=tk.X, pady=10)
        
        settings = ["Allow Comments", "Allow Duets", "Allow Stitch"]
        for setting in settings:
            var = tk.BooleanVar(value=True)
            cb = tk.Checkbutton(
                settings_frame,
                text=setting,
                variable=var,
                bg=self.colors["bg"],
                fg=self.colors["fg"],
                selectcolor=self.colors["border"]
            )
            cb.pack(anchor="w", padx=10, pady=5)
        
        return post_frame

    def create_schedule_content(self):
        schedule_frame = tk.Frame(
            self.content_area,
            bg=self.colors["bg"]
        )
        
        self.schedule_calendar = ScheduleCalendar(schedule_frame, self.colors)
        return schedule_frame

    def show_post_content(self):
        self.schedule_content.pack_forget()
        self.post_content.pack(fill=tk.BOTH, expand=True)

    def show_schedule_content(self):
        self.post_content.pack_forget()
        self.schedule_content.pack(fill=tk.BOTH, expand=True)

    def upload_media(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif"),
                ("Video files", "*.mp4 *.mov *.avi")
            ]
        )
        if file_path:
            print(f"Selected file: {file_path}")

class ScheduleCalendar:
    def __init__(self, parent, colors):
        self.parent = parent
        self.colors = colors
        self.current_date = datetime.now()
        self.scheduled_posts = {}
        
        self.create_calendar_interface()

    def create_calendar_interface(self):
        # Main container with padding
        self.container = tk.Frame(
            self.parent,
            bg=self.colors["bg"],
            padx=30,
            pady=20
        )
        self.container.pack(fill=tk.BOTH, expand=True)

        # Calendar header with month navigation
        self.header_frame = tk.Frame(
            self.container,
            bg=self.colors["bg"]
        )
        self.header_frame.pack(fill=tk.X, pady=(0, 20))

        # Previous month button
        self.prev_month = tk.Button(
            self.header_frame,
            text="◄",
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            bd=0,
            command=self.previous_month
        )
        self.prev_month.pack(side=tk.LEFT)

        # Month and year labels
        self.month_label = tk.Label(
            self.header_frame,
            text="January",
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            font=("Helvetica", 14)
        )
        self.month_label.pack(side=tk.LEFT, padx=10)

        # Previous/Next year buttons
        self.prev_year = tk.Button(
            self.header_frame,
            text="◄",
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            bd=0,
            command=self.previous_year
        )
        self.prev_year.pack(side=tk.LEFT, padx=(20, 0))

        self.year_label = tk.Label(
            self.header_frame,
            text="2024",
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            font=("Helvetica", 14)
        )
        self.year_label.pack(side=tk.LEFT, padx=10)

        self.next_year = tk.Button(
            self.header_frame,
            text="►",
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            bd=0,
            command=self.next_year
        )
        self.next_year.pack(side=tk.LEFT)

        # Next month button
        self.next_month = tk.Button(
            self.header_frame,
            text="►",
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            bd=0,
            command=self.next_month
        )
        self.next_month.pack(side=tk.LEFT, padx=(20, 0))

        # New Schedule button
        self.new_schedule_btn = tk.Button(
            self.header_frame,
            text="+ New Schedule",
            bg=self.colors["button"],
            fg=self.colors["fg"],
            padx=15,
            pady=5,
            bd=0,
            command=self.show_schedule_dialog
        )
        self.new_schedule_btn.pack(side=tk.RIGHT)

        # Calendar grid
        self.calendar_frame = tk.Frame(
            self.container,
            bg=self.colors["bg"]
        )
        self.calendar_frame.pack(fill=tk.BOTH, expand=True)

        # Weekday headers
        self.weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(self.weekdays):
            label = tk.Label(
                self.calendar_frame,
                text=day,
                bg=self.colors["bg"],
                fg=self.colors["fg"],
                font=("Helvetica", 10)
            )
            label.grid(row=0, column=i, pady=(0, 10))

        # Create calendar days
        self.day_frames = {}
        for row in range(6):
            for col in range(7):
                frame = tk.Frame(
                    self.calendar_frame,
                    bg=self.colors["sidebar"],
                    width=100,
                    height=100
                )
                frame.grid(row=row+1, column=col, padx=1, pady=1, sticky="nsew")
                frame.grid_propagate(False)
                
                day_label = tk.Label(
                    frame,
                    text="",
                    bg=self.colors["sidebar"],
                    fg=self.colors["fg"],
                    anchor="nw",
                    padx=5,
                    pady=5
                )
                day_label.pack(fill=tk.X)
                
                self.day_frames[f"{row+1},{col}"] = {
                    'frame': frame,
                    'label': day_label,
                    'content': tk.Frame(frame, bg=self.colors["sidebar"])
                }
                self.day_frames[f"{row+1},{col}"]['content'].pack(fill=tk.BOTH, expand=True)

        # Configure grid weights
        for i in range(7):
            self.calendar_frame.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.calendar_frame.grid_rowconfigure(i, weight=1)

        self.update_calendar()

    def update_calendar(self):
        # Update month and year labels
        self.month_label.config(text=self.current_date.strftime("%B"))
        self.year_label.config(text=str(self.current_date.year))

        # Clear existing calendar
        for frame_data in self.day_frames.values():
            frame_data['label'].config(text="")
            frame_data['frame'].config(bg=self.colors["sidebar"])
            
        # Get calendar data
        cal = calendar.monthcalendar(self.current_date.year, self.current_date.month)
        
        # Fill in days
        for row, week in enumerate(cal):
            for col, day in enumerate(week):
                if day != 0:
                    frame_data = self.day_frames[f"{row+1},{col}"]
                    frame_data['label'].config(text=str(day))
                    
                    # Highlight current day
                    if (day == self.current_date.day and 
                        self.current_date.month == datetime.now().month and 
                        self.current_date.year == datetime.now().year):
                        frame_data['frame'].config(bg=self.colors["button"])
                    
                    # Highlight days with scheduled posts
                    date_str = f"{self.current_date.year}-{self.current_date.month}-{day}"
                    if date_str in self.scheduled_posts:
                        self.add_schedule_indicator(frame_data['content'])

    def add_schedule_indicator(self, frame):
        indicator = tk.Frame(
            frame,
            bg=self.colors["button"],
            height=4
        )
        indicator.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

    def show_schedule_dialog(self):
        dialog = tk.Toplevel(self.parent)
        dialog.title("Schedule New Post")
        dialog.configure(bg=self.colors["bg"])
        dialog.geometry("400x500")

        # Time selection
        time_frame = tk.Frame(dialog, bg=self.colors["bg"], pady=10)
        time_frame.pack(fill=tk.X, padx=20)

        tk.Label(
            time_frame,
            text="Time:",
            bg=self.colors["bg"],
            fg=self.colors["fg"]
        ).pack(side=tk.LEFT)

        hour_var = tk.StringVar(value="12")
        minute_var = tk.StringVar(value="00")
        period_var = tk.StringVar(value="PM")

        hour_menu = ttk.Combobox(
            time_frame,
            textvariable=hour_var,
            values=[str(i).zfill(2) for i in range(1, 13)],
            width=3
        )
        hour_menu.pack(side=tk.LEFT, padx=5)

        tk.Label(
            time_frame,
            text=":",
            bg=self.colors["bg"],
            fg=self.colors["fg"]
        ).pack(side=tk.LEFT)

        minute_menu = ttk.Combobox(
            time_frame,
            textvariable=minute_var,
            values=[str(i).zfill(2) for i in range(0, 60, 5)],
            width=3
        )
        minute_menu.pack(side=tk.LEFT, padx=5)

        period_menu = ttk.Combobox(
            time_frame,
            textvariable=period_var,
            values=["AM", "PM"],
            width=3
        )
        period_menu.pack(side=tk.LEFT, padx=5)

        # Platform selection
        platform_frame = tk.LabelFrame(
            dialog,
            text="Platforms",
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            pady=10
        )
        platform_frame.pack(fill=tk.X, padx=20, pady=10)

        platforms = ["Facebook", "Instagram", "Twitter", "LinkedIn", "TikTok"]
        platform_vars = {}
        
        for platform in platforms:
            var = tk.BooleanVar()
            platform_vars[platform] = var
            tk.Checkbutton(
                platform_frame,
                text=platform,
                variable=var,
                bg=self.colors["bg"],
                fg=self.colors["fg"],
                selectcolor=self.colors["sidebar"]
            ).pack(anchor=tk.W)

        # Buttons
        button_frame = tk.Frame(dialog, bg=self.colors["bg"])
        button_frame.pack(side=tk.BOTTOM, pady=20)

        tk.Button(
            button_frame,
            text="Schedule",
            bg=self.colors["button"],
            fg=self.colors["fg"],
            command=lambda: self.save_schedule(
                hour_var.get(),
                minute_var.get(),
                period_var.get(),
                platform_vars,
                dialog
            )
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            button_frame,
            text="Cancel",
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            command=dialog.destroy
        ).pack(side=tk.LEFT, padx=5)

    def save_schedule(self, hour, minute, period, platform_vars, dialog):
        selected_date = self.calendar.get_date()
        time_str = f"{hour}:{minute} {period}"
        platforms = [p for p, v in platform_vars.items() if v.get()]
        
        if selected_date not in self.scheduled_posts:
            self.scheduled_posts[selected_date] = []
            
        self.scheduled_posts[selected_date].append({
            'time': time_str,
            'platforms': platforms
        })
        
        self.update_posts_display(selected_date)
        dialog.destroy()

    def on_date_select(self, event=None):
        selected_date = self.calendar.get_date()
        self.update_posts_display(selected_date)

    def update_posts_display(self, date):
        # Clear existing posts
        for widget in self.posts_scrollable_frame.winfo_children():
            widget.destroy()

        # Show scheduled posts for selected date
        if date in self.scheduled_posts:
            for post in self.scheduled_posts[date]:
                post_frame = tk.Frame(
                    self.posts_scrollable_frame,
                    bg=self.colors["sidebar"],
                    padx=10,
                    pady=10
                )
                post_frame.pack(fill=tk.X, pady=5)

                tk.Label(
                    post_frame,
                    text=post['time'],
                    bg=self.colors["sidebar"],
                    fg=self.colors["fg"],
                    font=('Helvetica', 12, 'bold')
                ).pack(anchor=tk.W)

                platforms_text = ", ".join(post['platforms'])
                tk.Label(
                    post_frame,
                    text=platforms_text,
                    bg=self.colors["sidebar"],
                    fg=self.colors["fg"]
                ).pack(anchor=tk.W)

    def previous_month(self):
        self.current_date = self.current_date.replace(day=1)  # Go to first day of current month
        self.current_date = self.current_date - timedelta(days=1)  # Go to last day of previous month
        self.current_date = self.current_date.replace(day=1)  # Go to first day of previous month
        self.update_calendar()

    def next_month(self):
        # If we're in December, we need to increment the year
        if self.current_date.month == 12:
            self.current_date = self.current_date.replace(year=self.current_date.year + 1, month=1)
        else:
            self.current_date = self.current_date.replace(month=self.current_date.month + 1)
        self.update_calendar()

    def previous_year(self):
        self.current_date = self.current_date.replace(year=self.current_date.year - 1)
        self.update_calendar()

    def next_year(self):
        self.current_date = self.current_date.replace(year=self.current_date.year + 1)
        self.update_calendar()

    def on_day_click(self, day):
        # Handle day selection
        self.selected_date = day
        self.update_calendar()
        # You can add more functionality here when a day is clicked

    def get_selected_date(self):
        return self.selected_date if hasattr(self, 'selected_date') else None

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x800")  # Set initial window size
    app = PostingInterface(root)
    root.mainloop()

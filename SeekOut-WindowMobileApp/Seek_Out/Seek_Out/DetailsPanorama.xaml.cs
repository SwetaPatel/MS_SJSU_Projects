/* 
 * Author: Sweta Patel (008671754) 
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Shapes;
using Microsoft.Phone.Controls;
using System.Windows.Media.Imaging;
using System.Device.Location;
using System.IO;
using System.Text;
using Microsoft.Phone.Shell;

namespace Seek_Out
{
 
    public partial class PanoramaPage1 : PhoneApplicationPage
    {
        static public string range = "No range";
        static public string Category = "No Category";
        public string finalCategory;       
        private string locationAPI = "https://maps.googleapis.com/maps/api/place/nearbysearch/xml?location=$value&radius=$range&types=$Category&sensor=false&key=AIzaSyDM8RoFHMgloaItNhafZ1FK7k4rxrvdRZY";
        Stream streamResult; 
        StreamReader objReader;
        string sLine; string result = "";
        StringBuilder sb;
        PanoramaItem pi;
        StackPanel sp;
        TextBlock t;
        Image img;
        int flag = 0;
        public static string lati;
        public static string longi;
        public PanoramaPage1()
        {
            InitializeComponent();            
            ApplicationBar = new ApplicationBar();
            ApplicationBarIconButton btnPin = new ApplicationBarIconButton(new Uri("/Images/pin.png", UriKind.RelativeOrAbsolute));
            btnPin.Text = "Push Pin";
            ApplicationBar.BackgroundColor = new Color { R = 0xFF, G = 0x1D, B = 0x51 };
            ApplicationBar.Buttons.Add(btnPin);
            btnPin.Click += new EventHandler(btnPin_Click);                 
        }
        
        protected override void OnNavigatedTo(System.Windows.Navigation.NavigationEventArgs e)
        {
            base.OnNavigatedTo(e);
            if (this.NavigationContext.QueryString.ContainsKey("Category"))
            {
                Category = this.NavigationContext.QueryString["Category"]; 
                range = this.NavigationContext.QueryString["range"];
                lati = this.NavigationContext.QueryString["lati"];
                longi = this.NavigationContext.QueryString["longi"];
            }
            if (lati == null || lati.Trim().Equals(""))
            {
                lati = ((App)App.Current).loc.lati;
            }
            if (longi == null || longi.Trim().Equals(""))
            {
                longi = ((App)App.Current).loc.longi;
            }            
            double finalrange = Convert.ToDouble(range.Substring(0, 2)) * 1609.34;            
            string url = locationAPI.Replace("$value",  lati + "," + longi);
            string url1 = url.Replace("$range", ""+finalrange);            
            switch (Category)
            { 
                case "btnFood":
                    finalCategory = "food";
                    break;
                case "btnATM":
                    finalCategory = "atm";
                    break;
                case "btnGas":
                    finalCategory = "gas_station";
                    break;
                case "btnParking":
                    finalCategory = "parking";
                    break;
                case "btnPolice":
                    finalCategory = "police";
                    break;
                case "btnHospital":
                    finalCategory = "hospital";
                    break;
                default:
                    finalCategory = "";
                    break;            
            }            
            string url2 = url1.Replace("$Category",finalCategory);
            exectueService(url2);            
        }
        public void exectueService(string Url)
        {
            UriBuilder fullUri = new UriBuilder(Url);
            HttpWebRequest serviceRequest = (HttpWebRequest)WebRequest.Create(fullUri.Uri);            
            ServiceExecutorUpdateState executionState = new ServiceExecutorUpdateState();
            executionState.AsyncRequest = serviceRequest;
            serviceRequest.BeginGetResponse(new AsyncCallback(HandleServiceExecutorResponse), executionState);
        }

        private void HandleServiceExecutorResponse(IAsyncResult asyncResult)
        {
            ServiceExecutorUpdateState executionState = (ServiceExecutorUpdateState)asyncResult.AsyncState;
            HttpWebRequest serviceRequest = (HttpWebRequest)executionState.AsyncRequest;
            executionState.AsyncResponse = (HttpWebResponse)serviceRequest.EndGetResponse(asyncResult);
            sb = new StringBuilder();
            try
            {
                streamResult = executionState.AsyncResponse.GetResponseStream();
                objReader = new StreamReader(streamResult);
                sLine = "";                
                processCategory();               
            }
            catch (FormatException)
            {           
                return;
            }
        }

        public void processCategory() {
            Dictionary<string,string> categoryAttributes = new Dictionary<string, string>();
            categoryAttributes.Add("<name", "</name>");
            categoryAttributes.Add("<vicinity", "</vicinity>");
            categoryAttributes.Add("<rating", "</rating>");
            categoryAttributes.Add("<open_now", "</open_now>");
            categoryAttributes.Add("<photo_reference", "</photo_reference>");
            categoryAttributes.Add("<price_level", "</price_level>"); 
            while ((sLine = objReader.ReadLine()) != null)
            {   
                if(sLine.Trim().Equals("</result>")){
                    sb.Append("|");
                }
                string[] splitArray = sLine.Split('>');
                if (categoryAttributes.ContainsKey(splitArray[0].Trim()))
                {
                    StringBuilder temp = new StringBuilder(sLine);
                    temp.Replace(splitArray[0].Trim() + ">", "");
                    temp.Replace(categoryAttributes[splitArray[0].Trim()], "");
                    switch(splitArray[0].Trim()){
                        case "<name":
                            sb.Append(temp + "$");
                            break;
                        case "<vicinity":
                            sb.Append("Vicinity: " + temp + "$");
                            break;
                        case "<Rating":
                            sb.Append("Rating: " + temp + "$");
                            break;
                        case "<open_now":
                            if (temp.ToString().Trim().Equals("true"))
                            {
                                sb.Append("Currently Open" + "$");
                            }
                            else
                            {
                                sb.Append("Currently Closed" + "$");
                            }                     
                            break;
                        case "<photo_reference":
                            sb.Append("*"+temp + "$");
                            break;
                        case "<price_level":
                            sb.Append("Price level: " + temp + "$");
                            break;
                    }                                   
                }                        
            }                      
            result = sb.ToString();            
            postMyMessage(result);
        }

        public class ServiceExecutorUpdateState
        {
            public HttpWebRequest AsyncRequest { get; set; }
            public HttpWebResponse AsyncResponse { get; set; }
        }

        private void postMyMessage(string text)
        {
            if (this.Dispatcher.CheckAccess()) {                
                string[] allEntries = text.Split('|');
                for (int i = 0; i < allEntries.Length-1; i++)
                {
                    flag = 0;
                    pi = new PanoramaItem();
                    sp = new StackPanel();
                    sp.HorizontalAlignment = System.Windows.HorizontalAlignment.Center;
                    string[] allAttributes = allEntries[i].Split('$');
                    pi.Header = allAttributes[0];
                    pi.Foreground = new SolidColorBrush(Colors.White);
                    pi.FontSize = 30;
                    for (int j = 1; j < allAttributes.Length; j++)
                    {
                        if (allAttributes[j].StartsWith("*"))
                        {
                            flag = 1;
                            String temp = allAttributes[j].Replace("*","");
                            img = new Image();
                            img.Height = 300; img.Width = 300;
                            img.Source = new BitmapImage(new Uri("https://maps.googleapis.com/maps/api/place/photo?maxwidth=200&photoreference="+temp+"&sensor=true&key=AIzaSyDM8RoFHMgloaItNhafZ1FK7k4rxrvdRZY"));
                            sp.Children.Add(img);
                            pi.Content = sp;
                        }
                        else
                        {
                            t = new TextBlock();
                            t.Foreground = new SolidColorBrush(Colors.White);
                            t.FontSize = 20;
                            if (allAttributes[j].Equals("Currently Open"))
                                t.Foreground = new SolidColorBrush(Colors.Green);
                            if (allAttributes[j].Equals("Currently Closed"))
                                t.Foreground = new SolidColorBrush(Colors.Red);
                            t.Text = allAttributes[j];
                            t.TextWrapping = TextWrapping.Wrap;
                            sp.Children.Add(t);
                            pi.Content = sp;
                        }                        
                    }
                    if (flag == 0) {
                        img = new Image();
                        img.Height = 300; img.Width = 300;                       
                        switch (finalCategory)
                        {
                            case "food":
                                img.Source = new BitmapImage(new Uri("/Images/DefaultFood.png", UriKind.Relative));
                                break;
                            case "atm":
                                img.Source = new BitmapImage(new Uri("/Images/DefaultATM1.png", UriKind.Relative));
                                break;
                            case "gas_station":
                                img.Source = new BitmapImage(new Uri("/Images/DefaultGas.png", UriKind.Relative));
                                break;
                            case "parking":
                                img.Source = new BitmapImage(new Uri("/Images/DefaultParking.png", UriKind.Relative));
                                break;
                            case "police":
                                img.Source = new BitmapImage(new Uri("/Images/DefaultPolice.png", UriKind.Relative));
                                break;
                            case "hospital":
                                img.Source = new BitmapImage(new Uri("/Images/DefaultHospital.png", UriKind.Relative));
                                break;
                            default:
                                break;
                        }                        
                        sp.Children.Add(img);
                        pi.Content = sp;
                    }
                    seek.Items.Add(pi);
                }
                   
            }
            else
                this.Dispatcher.BeginInvoke(new Action<string>(postMyMessage), text);
        }

        protected override void OnBackKeyPress(System.ComponentModel.CancelEventArgs e)
        {
            e.Cancel = true;
            NavigationService.Navigate(new Uri("/MainPage.xaml", UriKind.Relative));
        }
        
        void btnPin_Click(object sender, EventArgs e)
        {
            Uri mySecondaryPage = new Uri("/DetailsPanorama.xaml?Category=" + Category + "&range=" + range + "&lati=" + lati + "&longi=" + longi, UriKind.Relative);
            ShellTile tile = ShellTile.ActiveTiles.Where(x => x.NavigationUri == mySecondaryPage).FirstOrDefault();
            if (tile != null)
            {
                tile.Delete();
            }
            var newTile1 = new StandardTileData()
            {
                Title = finalCategory,
                BackgroundImage = new Uri("/Images/pin.png", UriKind.Relative)
            };
            ShellTile.Create(mySecondaryPage, newTile1);
        }
    }
}
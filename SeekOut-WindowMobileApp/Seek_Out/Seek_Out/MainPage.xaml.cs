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
using System.Device.Location;
using System.IO;
using System.Text;
using Microsoft.Phone.Shell;


namespace Seek_Out
{   /* PLEASE CHANGE CURRENT LOCATION FROM EMULATOR:
        1) Click on >> icon from Emulator's right side available options.
        2) Go to Location tab.
        3) Enter your current location in Search textbox and click on Enter.
        4) Click on any perticular area of map to locate current location.
        5) Now run the application. It will display current location on the Main page of application.     
     */
    public partial class MainPage : PhoneApplicationPage
    {
        // Constructor
        private string mapsAPI = "http://maps.googleapis.com/maps/api/geocode/xml?latlng=$value&sensor=true";
        string result = "";
        static string Category="";
        static string range="";
        public static string result1="No address";
        
        public MainPage()
        {
            InitializeComponent();
            ApplicationBar = new ApplicationBar();
            ApplicationBarIconButton btnSearch = new ApplicationBarIconButton(new Uri("/Images/search.png", UriKind.Relative));
            btnSearch.Text = "Search";
            ApplicationBar.BackgroundColor = new Color{R=0xFF, G=0x1D, B=0x51};
            ApplicationBar.Buttons.Add(btnSearch); 
            btnSearch.Click += new EventHandler(btnSearch_Click);

            ApplicationBarIconButton btnPin = new ApplicationBarIconButton(new Uri("/Images/pin.png", UriKind.Relative));
            btnPin.Text = "Push Pin";
            ApplicationBar.Buttons.Add(btnPin);
            btnPin.Click += new EventHandler(btnPin_Click);     
            
            ShellTile appTile = ShellTile.ActiveTiles.First();
            if (appTile != null)
            {
                StandardTileData newTile1 = new StandardTileData
                {
                    BackgroundImage = new Uri("/Images/splash.png", UriKind.Relative),
                };
                appTile.Update(newTile1);
            }
        }

        void btnPin_Click(object sender, EventArgs e)
        {
            Uri mySecondaryPage = new Uri("/MainPage.xaml?result="+result, UriKind.Relative);
            ShellTile tile = ShellTile.ActiveTiles.Where(x => x.NavigationUri == mySecondaryPage).FirstOrDefault();
            if (tile != null)
            {
                tile.Delete();
            }

            StandardTileData newTile = new StandardTileData();           
            newTile.BackgroundImage = new Uri("/Images/splash.png", UriKind.Relative);
            ShellTile.Create(mySecondaryPage, newTile);             
        }

        void btnSearch_Click(object sender, EventArgs e)
        {
            if (Category == null || Category.Trim().Equals("") || range == null || range.Trim().Equals("")) {           
                MessageBox.Show("Please select search Category and Range. ");
            }
            else{
            NavigationService.Navigate(new Uri("/DetailsPanorama.xaml?Category=" + Category + "&range=" + range + "&lati=" + ((App)App.Current).loc.lati+ "&longi="+ ((App)App.Current).loc.longi, UriKind.Relative));            
            }
        }
       
        protected override void OnNavigatedTo(System.Windows.Navigation.NavigationEventArgs e)
        {
            base.OnNavigatedTo(e);
            if (this.NavigationContext.QueryString.ContainsKey("result"))
            {
                result1 = this.NavigationContext.QueryString["result"];               
                txtCurrentAddress.Text = result1;                
            }           
            else
            {
                string url = mapsAPI.Replace("$value", (((App)App.Current).loc.lati + "," + ((App)App.Current).loc.longi));
                exectueService(url);
            }            
            while (NavigationService.BackStack.Any())
              NavigationService.RemoveBackEntry();              
        }   

        private void PhoneApplicationPage_Loaded(object sender, RoutedEventArgs e)
        {          

        }

        public void postMyMessage(string text)
        {
            if (this.Dispatcher.CheckAccess())
                txtCurrentAddress.Text = text;
            else
               this.Dispatcher.BeginInvoke(new Action<string>(postMyMessage), text);
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
            StringBuilder sb = new StringBuilder();
            try
            {
                Stream streamResult = executionState.AsyncResponse.GetResponseStream();
                StreamReader objReader = new StreamReader(streamResult);
                string sLine = "";
                while ((sLine = objReader.ReadLine()) != null)
                {
                    if (sLine.Trim().StartsWith("<formatted_address>"))
                    {
                        sb.Append(sLine);
                        break;
                    }
                }
                sb.Replace("<formatted_address>", "");
                sb.Replace("</formatted_address>", "");
                result = sb.ToString();
                postMyMessage(result);
            }
            catch (FormatException)
            {
                return;
            }
        }

        public class ServiceExecutorUpdateState
        {
            public HttpWebRequest AsyncRequest { get; set; }
            public HttpWebResponse AsyncResponse { get; set; }
        }

        private void btnCategory_Click(object sender, RoutedEventArgs e)
        {
           btnATM.BorderBrush = new SolidColorBrush(Colors.Transparent);
           btnFood.BorderBrush = new SolidColorBrush(Colors.Transparent);
           btnPolice.BorderBrush = new SolidColorBrush(Colors.Transparent);
           btnHospital.BorderBrush = new SolidColorBrush(Colors.Transparent);
           btnGas.BorderBrush = new SolidColorBrush(Colors.Transparent);
           btnParking.BorderBrush = new SolidColorBrush(Colors.Transparent); 
           ((Button)sender).BorderBrush = new SolidColorBrush(Colors.Red);
           Category = ((Button)sender).Name;           
        }

        private void lstRadius_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            range = ((ListBoxItem)lstRadius.SelectedItem).Content.ToString();
        }           
    }
}
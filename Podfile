source 'https://github.com/CocoaPods/Specs.git'
platform :ios, '13.0'
use_frameworks!

target 'Blueverse' do
    pod "FLUtilities", :git => 'https://github.com/Nickelfox/FLUtilities.git'
    pod "FLLogs", :git => 'https://github.com/Nickelfox/FLLogs.git', :branch => 'develop'
    pod "AnyErrorKit", :git => 'https://github.com/Nickelfox/AnyErrorKit.git'
    pod 'Kingfisher'
    pod 'MBProgressHUD'
    pod 'SwiftLint'
    pod 'AppCenter'
end

target 'Model' do
    pod "FLUtilities", :git => 'https://github.com/Nickelfox/FLUtilities.git'
    pod "FLLogs", :git => 'https://github.com/Nickelfox/FLLogs.git', :branch => 'develop'
    pod 'FoxAPIKit', :git => 'https://github.com/Nickelfox/FoxAPIKit.git', :branch => 'develop'
end

post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['SWIFT_VERSION'] = '5.0'
      config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '15.0'
    end
  end
end
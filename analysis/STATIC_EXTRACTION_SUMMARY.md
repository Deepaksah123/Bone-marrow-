# Static APK extraction summary

Source: `base.apk`
SHA-256: `e03a582c20eec102510509918315be53e45bb9fe90647207b2c956a0f55316a3`
Size: 72,425,656 bytes

## Package / app namespace indicators

`com.marrow2`

## App-specific class indicators recovered from DEX strings

- com.marrow2.ui.home.HomeViewModelV2
- com.marrow2.ui.home.ZenAreaViewModel
- com.marrow2.ui.payment.PaymentViewModel
- com.marrow2.ui.qbank.play.QBankMcqViewModel
- com.marrow2.ui.qbank.play.QBankPlayViewModel
- com.marrow2.ui.test.score.TestScoreViewModel
- com.marrow2.ui.mcq.component.McqVideoPlayer
- com.marrow2.ui.mcq.component.VideoControlBar
- com.marrow2.ui.mcq.component.PlaybackControl
- com.marrow2.ui.mcq.component.VideoSurface
- com.marrow2.ui.mcq.component.VideoThumbnail
- com.marrow2.ui.mcq.component.BufferingLoader
- com.marrow2.ui.mcq.component.CenterPlayOverlay
- com.marrow2.ui.qbank.score.compose.ScoreContent
- com.marrow2.ui.qbank.score.compose.ScoreToolbar
- com.marrow2.ui.qbank.score.compose.SchemaItem
- com.marrow2.ui.qbank.score.compose.SchemaSection
- com.marrow2.ui.qbank.score.compose.StatRow
- com.marrow2.ui.qbank.score.compose.StatItem
- com.marrow2.ui.test.gtanalytics.composable.GtaLoader
- com.marrow2.ui.test.landing.composable.NewTag
- com.marrow2.ui.internal_web.ui.main.InternalWebViewModel
- com.marrow2.core.common_composables.FilterIcon

## Manifest activity/service indicators

The binary manifest contains indicators for activities/services including:

- com.marrow2...TrainingApplication
- ...ui.activities.learn.video.LessonVideoActivity
- ...ui.activities.onboarding.deeplinkroute.DeeplinkActivity
- ...ui.activities.onboarding.deeplinkroute.DeeplinkProcessorActivity
- ...ui.activities.onboarding.splash.SplashActivity
- ...ui.activities.plan.PlanActivity
- ...ui.activities.plan.renew.RenewActivity
- ...ui.activities.web.payment.PaymentInternalWebActivity
- ...kt.ui.activities.sync.SyncingActivity
- ...bgservices.PushReceiverService
- ...bgservices.imageupload.ImageUploadService
- ...services.NetworkAvailableJobService

The exact package-qualified names for some obfuscated manifest entries require a proper binary-XML decoder to reconstruct.

## DEX layout

- classes.dex — 11,815,996 bytes
- classes2.dex — 9,311,104 bytes
- classes3.dex — 13,516,816 bytes
- classes4.dex — 11,442,620 bytes
- classes5.dex — 6,234,216 bytes

## Native libraries

Four ABIs are present: arm64-v8a, armeabi-v7a, x86, x86_64.

Libraries observed under each ABI include:

- liba25339.so
- libb2ef44.so
- libc59f88.so
- libd9.so
- libe938.so

## Major embedded frameworks / SDK indicators

- Jetpack Compose / Compose Material / Material3
- Kotlin coroutines
- ExoPlayer
- Firebase / Crashlytics / Performance / Messaging
- Facebook SDK
- CleverTap
- Mixpanel
- Razorpay
- PhonePe
- Juspay HyperSDK / HyperPay / payment assets
- Google Play Services / Billing / Integrity / Maps
- Lottie
- Glide
- ML Kit barcode components
- React Native classes are also present in the dependency set

## Embedded application assets

- Roboto, Open Sans, Georgia and Helvetica fonts
- Lottie animations including zen-area, marrowthon, completion and revision animations
- CSS files including light/dark/sepia description themes, pearl.css, fc.css and select2.min.css
- Juspay payment bundles and configuration
- baseline profile / dexopt assets
- web HTML assets

## Important limitation

This file records only verified static extraction results. Java/Kotlin source reconstruction, Smali generation and decoded Android resources require a dedicated APK/Dex decompiler. No such binary is installed in the current runtime, so no fabricated “decompiled source” is included.

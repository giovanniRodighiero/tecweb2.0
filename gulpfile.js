var pug = require('gulp-pug');
var gulp = require('gulp');
var sass = require('gulp-sass');
var ext_replace = require('gulp-ext-replace');

gulp.task('xml', function buildHTML() {
  return gulp.src('assets/xml/**/*.pug')
  .pipe(pug({
    pretty: true,
    doctype: 'xml'
    // Your options in here.
  }))
  .pipe(ext_replace('.xml'))
  .pipe(gulp.dest('public_html/xml/'))
});
gulp.task('xsl', function buildHTML() {
  return gulp.src('assets/xsl/**/*.pug')
  .pipe(pug({
    pretty: true
    // Your options in here.
  }))
  .pipe(ext_replace('.xsl'))
  .pipe(gulp.dest('public_html/xsl/'))
});
gulp.task('style', () => {
  return gulp.src('assets/style/**/*.sass')
  .pipe(sass().on('error', sass.logError))
  .pipe(gulp.dest('public_html/style/'));
})
gulp.task('watch', function(){
  gulp.watch('assets/xml/**/*.pug', ['xml']);
  gulp.watch('assets/xsl/**/*.pug', ['xsl']);
  gulp.watch('assets/style/**/*.sass', ['style']);
});

gulp.task('default', ['xml','xsl','style','watch']);

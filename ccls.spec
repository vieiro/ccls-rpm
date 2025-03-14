#
# ccls
# A C, C++ and Objective-C LSP Language Server.
# Apache-2.0
#

Name:          ccls
Version:       0.20241108
Release:       1
Summary:       A C/C++/Objective-C LSP language server

License:       Apache-2.0
URL    :       https://github.com/MaskRay/ccls
Source0:       https://github.com/MaskRay/ccls/archive/refs/tags/%{version}.tar.gz
Source1:       ccls.md

BuildRequires: cmake
BuildRequires: rapidjson-devel
BuildRequires: pandoc

BuildRequires: clang
BuildRequires: clang-devel
BuildRequires: llvm-devel

Requires     : llvm-libs

%description
ccls is a LSP language server for C, C++ and Objective-C.

It provides code completion, definition, references, cross-references,
formatting, call hierarchies, inheritance hierarchies, member hierarchies,
symbol renaming, hover information, diagnostics and code actions and
semantic highlighting and navigation for editors that support the
LSP protocol, such as "Emacs" or "Neovim".

%prep
%autosetup

%build
# Generate the man page
pandoc --standalone --to man %{SOURCE1} -o ccls.1
# Compress the man page
gzip ccls.1
# Generate a Makefile for release in the "build" directory
cmake -DCCLS_VERSION=%{version} -DCMAKE_PREFIX_PATH=/usr/lib64/cmake/llvm -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -S. -Bbuild
# Perform a release build in the "build" directory
cmake --build build
# Test: print out the ccls version
./build/ccls --version

%install

# Cleanup the buildroot and create directories for files
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
# Install files with permissions
install -m 755 Release/ccls %{buildroot}/%{_bindir}/ccls
install -m 644 ccls.1.gz %{buildroot}/%{_mandir}/man1/ccls.1.gz

%files
%{_bindir}/ccls
%{_mandir}/man1/ccls.1.gz
%license LICENSE

%changelog
* Fri Mar 14 2025 Antonio Vieiro <vieiro@gmail.com> - 0.20241108-1
- Initial version



